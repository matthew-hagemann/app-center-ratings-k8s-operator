# Copyright 2023 Canonical
# See LICENSE file for licensing details.

import unittest

# from unittest.mock import patch
from ratings import Ratings


class TestRatings(unittest.TestCase):
    def setUp(self):
        pass

    def test_ratings_constructor_props(self):
        r = Ratings("foobar", "deadbeef")
        self.assertEqual(r.connection_string, "foobar")
        self.assertEqual(r.jwt_secret, "deadbeef")

    def test_ratings_pebble_layer(self):
        r = Ratings("foobar", "deadbeef")
        self.assertEqual(
            r.pebble_layer(),
            {
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
                            "APP_JWT_SECRET": "deadbeef",
                            "APP_POSTGRES_URI": "foobar",
                            "APP_MIGRATION_POSTGRES_URI": "foobar",
                            "APP_LOG_LEVEL": "info",
                        },
                    }
                },
            },
        )
