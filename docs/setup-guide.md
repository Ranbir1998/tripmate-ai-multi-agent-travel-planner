# Local Setup Guide (Windows)

See the root [README](../README.md) for the quick start. These notes cover common failures.

## Dependencies

Use a Python virtual environment and run `python -m pip install -r requirements.txt` plus `python -m pip install uv`. Confirm the AviationStack launcher with `uvx --version`.

## Services

1. Start Docker Desktop and the PostgreSQL container (`docker start multiagent-postgres` for an existing container).
2. Check readiness with `docker exec multiagent-postgres pg_isready`.
3. Start Ollama on `localhost:11434`, ensure `qwen2:7b` is available (`ollama list`), and verify `/api/tags`.
4. Copy `.env.example` to `.env`, set `DATABASE_URL`, and add optional provider keys.
5. Start FastAPI: `python -m uvicorn app:app --host 127.0.0.1 --port 8000 --reload`.
6. Open `http://127.0.0.1:8000`.

## Troubleshooting

| Symptom | Check |
|---|---|
| PostgreSQL connection timeout | Docker Desktop, running container, database URL, port 5432 |
| Ollama connection refused | Ollama server status, port 11434, installed model |
| `uvx` not found | Activate `.venv`, install `uv`, then run `uvx --version` |
| AviationStack `function_access_restricted` | Your account's plan and permitted API functions |
| OpenWeather HTTP 401 | Correct/active key; revoke leaked keys and check service access |
| MCP invocation returns an error inside `SUCCESS` | Read response payload; errors can be returned as tool-result text |
| Missing approval buttons after revision | Known frontend HITL issue; see `docs/testing.md` |

## Database URL

Use `postgresql://USER:PASSWORD@HOST:PORT/DBNAME` with values matching the running PostgreSQL container. Do not commit real credentials.
