"""
This module provides configuration utilities for the application, including
environment variable loading and SQLAlchemy database URI construction.
Functions:
    get_env_var(key, fallback_dict): Retrieves the value of an environment variable,
        falling back to a provided dictionary (typically loaded from a .env file)
        if the variable is not set in the environment.
Classes:
    Config: Contains application configuration constants, including the SQLAlchemy
        database URI and tracking modification settings.
"""

import os
from dotenv import dotenv_values
from sqlalchemy.pool import StaticPool

# Load from .env file (as fallback)
fallback_env = dotenv_values(".env")


def get_env_var(key, fallback_dict=fallback_env):
    """TODO: Write docstring."""
    return os.environ.get(key, fallback_dict.get(key))


def _is_sqlite_mode():
    val = get_env_var("USE_SQLITE")
    return val is not None and val.strip().lower() in ("true", "1", "yes")


class Config:
    """TODO: Write docstring."""

    if _is_sqlite_mode():
        SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
        SQLALCHEMY_ENGINE_OPTIONS = {
            "connect_args": {"check_same_thread": False},
            "poolclass": StaticPool,
        }
    else:
        SQLALCHEMY_DATABASE_URI = (
            f"mysql+mysqlconnector://{get_env_var('DB_USER')}:{get_env_var('DB_PASSWORD')}"
            f"@{get_env_var('DB_HOST')}:{int(get_env_var('DB_PORT'))}/{get_env_var('DB_NAME')}"
        )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
