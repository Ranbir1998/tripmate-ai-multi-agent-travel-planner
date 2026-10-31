import asyncio
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

from mcp_client import (
    tavily_mcp_search,
    aviation_mcp_call,
    weather_mcp_search,
)


async def test_tavily():
    print("\n========== TAVILY API TEST ==========")

    try:
        result = await asyncio.wait_for(
            tavily_mcp_search(
                "Best hotels in Tokyo Japan for tourists"
            ),
            timeout=60,
        )

        print("STATUS: SUCCESS")
        print("RESULT:")
        print(str(result)[:1500])

    except Exception as exc:
        print("STATUS: FAILED")
        print(f"ERROR: {type(exc).__name__}: {exc}")


async def test_aviationstack():
    print("\n========== AVIATIONSTACK API TEST ==========")

    try:
        result = await asyncio.wait_for(
            aviation_mcp_call("list_airports"),
            timeout=60,
        )

        print("STATUS: SUCCESS")
        print("RESULT:")
        print(str(result)[:1500])

    except Exception as exc:
        print("STATUS: FAILED")
        print(f"ERROR: {type(exc).__name__}: {exc}")


async def test_weather():
    print("\n========== OPENWEATHER API TEST ==========")

    try:
        result = await asyncio.wait_for(
            weather_mcp_search("Tokyo"),
            timeout=60,
        )

        print("STATUS: SUCCESS")
        print("RESULT:")
        print(str(result)[:1500])

    except Exception as exc:
        print("STATUS: FAILED")
        print(f"ERROR: {type(exc).__name__}: {exc}")


async def main():
    await test_tavily()
    await test_aviationstack()
    await test_weather()


if __name__ == "__main__":
    asyncio.run(main())