# MCP Sample

A minimal [Model Context Protocol](https://modelcontextprotocol.io/) example with a Python MCP server and client. The server exposes `add`, `subtract`, `multiply`, and `divide` tools. The client starts the server over stdio, discovers those tools, and calls each one with `10` and `20`.

## Requirements

- Python 3.10 or later

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Run the example

```bash
python client.py
```

Expected logs include a successful connection, all four available tools, and these results:

- `add`: `30`
- `subtract`: `-10`
- `multiply`: `200`
- `divide`: `0.5`

## Project files

- `server.py` defines an MCP 2.x `MCPServer` named `My first server` and its calculator tools: `add(a, b)`, `subtract(a, b)`, `multiply(a, b)`, and `divide(a, b)`.
- `client.py` starts the server as a subprocess, initializes an MCP session, lists its tools, and calls each calculator tool sequentially.
- `requirements.txt` lists the Python dependency.

Both programs emit operational logs to stderr. This is important for the server: its stdout is reserved for MCP JSON-RPC messages when using the stdio transport.
