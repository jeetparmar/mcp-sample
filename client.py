import asyncio
import logging
import sys
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
    stream=sys.stderr,
)
logger = logging.getLogger(__name__)


async def main():
    server_params = StdioServerParameters(
        command=sys.executable,
        args=[str(Path(__file__).parent / "server.py")],
        env=None,
    )
    logger.info("Starting MCP server: %s %s", server_params.command, server_params.args[0])

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            logger.info("Initializing MCP session")
            await session.initialize()
            logger.info("MCP session initialized")
            logger.info("Connected to MCP server")

            tools_result = await session.list_tools()
            logger.info("Received %d tool(s) from the server", len(tools_result.tools))

            for tool in tools_result.tools:
                logger.info("Available tool: %s: %s", tool.name, tool.description or "No description")

            arguments = {"a": 10, "b": 20}
            logger.info("Calling add with arguments %s", arguments)
            result = await session.call_tool("add", arguments=arguments)
            logger.info("add completed with %d content item(s)", len(result.content))

            for content in result.content:
                if content.type == "text":
                    logger.info("Tool result: %s", content.text)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception:
        logger.exception("MCP client failed")
        raise
