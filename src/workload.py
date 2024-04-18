import logging
from dataclasses import dataclass
from enum import Enum
from typing import Optional

import ops
from entities import About, LogLevel, WorkloadEnv
from utils import get_or_fail

logger = logging.getLogger(__name__)


class WorkloadAgentBuilderState(Enum):
    DatabaseNotReady = "DatabaseNotReady"
    IngressNotReady = "IngressNotReady"
    EnvNotSet = "EnvNotSet"
    JwtSecretNotSet = "JwtSecretNotSet"
    Ready = "All config values set"


@dataclass
class WorkloadAgent:
    env: WorkloadEnv

    model: str
    name: str
    port: int
    log_level: LogLevel

    jwt_secret: str

    db_name: str
    db_relation_name: str
    db_host: str
    db_port: int
    db_username: str
    db_password: str

    @property
    def external_hostname(self) -> str:
        switch = {
            WorkloadEnv.Prod: "ratings.ubuntu.com",
            WorkloadEnv.Stg: "ratings.stg.ubuntu.com",
            WorkloadEnv.Local: "ratings.ubuntu.local",
        }

        return switch[self.env]

    @property
    def create_ingress_config(self) -> dict:
        routers = {
            self.name: {
                "rule": f"Host(`{self.external_hostname}`)",
                "service": f"{self.name}-service",
                "entryPoints": ["web"],
            }
        }

        services = {
            f"{self.name}-service": {
                "loadBalancer": {
                    "servers": [
                        {"url": f"h2c://{self.name}.{self.model}.svc.cluster.local:{self.port}"}
                    ]
                }
            }
        }

        return {"http": {"routers": routers, "services": services}}

    @property
    def create_pebble_layer(self) -> ops.pebble.Layer:
        db_connection_string = f"postgresql://{self.db_username}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

        environment: dict = {
            "APP_ENV": self.env.value,
            "APP_HOST": "0.0.0.0",
            "APP_LOG_LEVEL": self.log_level.value,
            "APP_JWT_SECRET": self.jwt_secret,
            "APP_NAME": self.name,
            "APP_PORT": self.port,
            "APP_POSTGRES_URI": db_connection_string,
            "APP_MIGRATION_POSTGRES_URI": db_connection_string,
            "APP_ADMIN_USER": "shadow",
            "APP_ADMIN_PASSWORD": "maria",
        }

        layer = ops.pebble.Layer(
            {
                "summary": "app-center-ratings pebble layer",
                "services": {
                    self.name: {
                        "override": "replace",
                        "summary": f"{self.name} pebble config layer",
                        "startup": "enabled",
                        "command": "/app/ratings",
                        "environment": environment,
                    }
                },
            }
        )
        return layer

    def api_url(self, path="") -> str:
        return f"http://localhost:{self.port}/{path}"

    def fetch_version(self) -> str:
        about = About(version="0.0.1")
        return about.version


class WorkloadAgentBuilder:
    """This is some context.

    - values that are known should be set
    - values that come from an event / relation should be wrapped in Optional
    - in theory, this is the only file that need be edited to take this template and create a new charm.
    """

    def __init__(self) -> None:
        self.model = "desktop"
        self.env: Optional[WorkloadEnv] = None
        self.name = "app-ratings"
        self.port = 8080
        self.jwt_secret: Optional[str]

        self.db_name = "ratings"
        self.db_relation_name = "database"
        self.db_host: Optional[str] = None
        self.db_port: Optional[int] = None
        self.db_username: Optional[str] = None
        self.db_password: Optional[str] = None

        """The ingress provider is Traefik."""
        self.ingress_relation_name = "ingress"
        self.ingress_ready = False

        """These options are to wire up the workload to the observability stack."""
        self.log_level = LogLevel.Info
        self.log_file = "/var/log/workload.log"
        self.log_relation_name = "log-proxy"
        self.grafana_relation_name = "grafana-dashboard"
        self.metrics_relation_name = "metrics-endpoint"

    def load_config_values(self, config: ops.ConfigData) -> "WorkloadAgentBuilder":
        self.set_env(config.get("env", ""))
        self.set_jwt_secret(config.get("jwt_secret", ""))
        self.set_log_level(config.get("log_level", ""))
        return self

    def set_env(self, value: str) -> "WorkloadAgentBuilder":
        self.env = WorkloadEnv.try_from_string(value)
        return self

    def set_db_host(self, value: str) -> "WorkloadAgentBuilder":
        self.db_host = value
        return self

    def set_db_port(self, value: int) -> "WorkloadAgentBuilder":
        self.db_port = value
        return self

    def set_db_username(self, value: str) -> "WorkloadAgentBuilder":
        self.db_username = value
        return self

    def set_db_password(self, value: str) -> "WorkloadAgentBuilder":
        self.db_password = value
        return self

    def set_ingress_ready(self, value: bool = True) -> "WorkloadAgentBuilder":
        self.ingress_ready = value
        return self

    def set_log_level(self, value: str) -> "WorkloadAgentBuilder":
        self.log_level = LogLevel.try_from_string(value)
        return self

    def set_jwt_secret(self, value: str) -> "WorkloadAgentBuilder":
        self.jwt_secret = value
        return self

    def get_state(self) -> WorkloadAgentBuilderState:
        db_ready = all(
            value is not None
            for value in [
                self.db_host,
                self.db_port,
                self.db_username,
                self.db_password,
            ]
        )

        if not db_ready:
            return WorkloadAgentBuilderState.DatabaseNotReady

        if not self.jwt_secret:
            return WorkloadAgentBuilderState.JwtSecretNotSet

        if not self.env:
            return WorkloadAgentBuilderState.EnvNotSet

        if not self.ingress_ready:
            return WorkloadAgentBuilderState.IngressNotReady

        return WorkloadAgentBuilderState.Ready

    def build(self) -> WorkloadAgent:
        return WorkloadAgent(
            env=get_or_fail(self.env, "env"),
            model=self.model,
            name=self.name,
            port=self.port,
            jwt_secret=get_or_fail(self.jwt_secret, "jwt_secret"),
            log_level=self.log_level,
            db_name=self.db_name,
            db_relation_name=self.db_relation_name,
            db_host=get_or_fail(self.db_host, "db_host"),
            db_port=get_or_fail(self.db_port, "db_port"),
            db_username=get_or_fail(self.db_username, "db_username"),
            db_password=get_or_fail(self.db_password, "db_password"),
        )
