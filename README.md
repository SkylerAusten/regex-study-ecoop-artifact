# Text-to-Regex Study (ECOOP Artifact)

A Flask web application for evaluating human performance on regex pattern matching tasks.

## Running with Docker

### Option 1: In-memory mode (no external database)

Run the container standalone with an ephemeral SQLite database -- no MySQL required. Data does not persist across restarts.

```bash
docker run -p 8080:8080 -e USE_SQLITE=true ghcr.io/skylerausten/regex-study-ecoop-artifact:latest
```

The app will be available at `http://localhost:8080`.

### Option 2: With MySQL (persistent data)

Use the provided compose file to run the app with a MySQL 8.4 database:

```bash
docker compose -f docker-compose.artifact.yml up
```

This starts both the MySQL database and the application. Data is persisted in a Docker volume.

## Running locally (development)

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Start in in-memory mode:
   ```bash
   USE_SQLITE=true python app.py
   ```

   Or configure MySQL via environment variables (`DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`, `DB_NAME`) or a `.env` file.
