#!/usr/bin/env python3
# Copyright 2023 Canonical
# See LICENSE file for licensing details.

"""Initialise and interact with the ratings service."""

import logging

logger = logging.getLogger(__name__)


class Ratings:
    """Represents the Ratings application."""

    def __init__(self, connection_string: str, jwt_secret: str):
        self.connection_string = connection_string
        self.jwt_secret = jwt_secret

    def ready(self):
        """Report whether Ratings is ready to start."""
        jwt_secret_present = len(self.jwt_secret) > 0
        connection_string_present = len(self.connection_string) > 0

        if not jwt_secret_present:
            logger.warning("Ratings service JWT token has zero-length")
        if not connection_string_present:
            logger.warning("Ratings service connection string is empty")

        return jwt_secret_present and connection_string_present

    def pebble_layer(self) -> dict:
        """Return a dictionary representing a Pebble layer."""
        return {
            "summary": "ratings layer",
            "description": "pebble config layer for ratings",
            "services": {
                "ratings": {
                    "override": "replace",
                    "summary": "ratings",
                    "command": "/bin/ratings",
                    "startup": "enabled",
                    "environment": {
                        "APP_ENV": "dev",
                        "APP_JWT_SECRET": self.jwt_secret,
                        "APP_POSTGRES_URI": self.connection_string,
                        "APP_MIGRATION_POSTGRES_URI": self.connection_string,
                        "APP_LOG_LEVEL": "info",
                    },
                }
            },
        }
