import asyncio
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

from mcp_client import client

SERVERS = ["tavily", "aviationstack", "weather"]


async def main():
    for server in SERVERS:
        print(f"\n{'=' * 50}")
        print(f"TESTING: {server.upper()}")
        print("=" * 50)

        try:
            tools = await asyncio.wait_for(
                client.get_tools(server_name=server),
                timeout=60,
            )

            print("STATUS: CONNECTED")
            print(f"TOOLS FOUND: {len(tools)}")

            for tool in tools:
                print(f" - {tool.name}")

        except Exception as exc:
            print("STATUS: FAILED")
            print(f"ERROR TYPE: {type(exc).__name__}")
            print(f"ERROR: {exc}")


if __name__ == "__main__":
    asyncio.run(main())