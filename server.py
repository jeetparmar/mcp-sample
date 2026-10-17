import logging
import sys

from mcp.server.mcpserver import MCPServer


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
    stream=sys.stderr,
)
logger = logging.getLogger(__name__)

mcp = MCPServer("My first server")


@mcp.tool()
def add(a: int, b: int) -> int:
    result = a + b
    logger.info("add called with a=%s, b=%s; returning %s", a, b, result)
    return result


if __name__ == "__main__":
    logger.info("Starting MCP server over stdio")
    mcp.run(transport="stdio")
