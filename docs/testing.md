# Verification and Known Limitations

## What has been observed

| Capability | Evidence | Assessment |
|---|---|---|
| Web UI and FastAPI | Local browser and request flows exercised | Working locally |
| Local Ollama | Qwen2:7b generated travel content | Working locally |
| PostgreSQL | Connection and checkpointed workflow execution | Working locally |
| Guardrail | A non-travel Java HashMap prompt was rejected | Observed working |
| Human approval | Initial draft and feedback-based revision were observed | Partial; repeated approval UI remains broken |
| Tavily MCP | 5 tools discovered; hotel search returned Tokyo results | Connected, data retrieved |
| AviationStack MCP | 13 tools discovered; `list_airports` returned `function_access_restricted` | Connected, endpoint denied by subscription |
| Weather MCP | 2 tools discovered; `get_current_weather` returned HTTP 401 | Connected, provider authentication failed |
| Budgets | Model generated totals inconsistent with listed expenses | Not reliable without validation |

## Reproduce MCP diagnostics

```powershell
python test_mcp_connections.py
python test_mcp_api.py
```

The first test discovers available tools; the second invokes sample API requests. These are diagnostic scripts, not assertion-driven tests. **Inspect response content carefully**: an MCP transport can succeed while the provider returns an error as text. Do not include API keys or raw secret-bearing URLs in shared logs.

## Planned improvements

- Redact API keys and URLs from tool-error logging.
- Build deterministic budget checks from structured line-item amounts.
- Restore approval controls after each feedback iteration.
- Add assertion-based unit/integration tests and CI.
- Handle missing provider access with clear UI explanations.
- Introduce source citations, travel-date validation, and provenance distinctions for estimates versus live data.
