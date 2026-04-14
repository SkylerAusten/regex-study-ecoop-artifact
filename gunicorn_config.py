import os

bind = "0.0.0.0:8080"

_use_sqlite = os.environ.get("USE_SQLITE", "").strip().lower() in ("true", "1", "yes")
workers = 1 if _use_sqlite else 2
