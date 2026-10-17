# MCP Sample

A minimal [Model Context Protocol](https://modelcontextprotocol.io/) example with a Python MCP server and client. The server exposes an `add` tool; the client starts the server over stdio, discovers that tool, and calls it with `10` and `20`.

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

Expected output includes a successful connection, the available `add` tool, and the result `30`.

## Project files

- `server.py` defines an MCP 2.x `MCPServer` named `My first server` and its `add(a, b)` tool.
- `client.py` starts the server as a subprocess, initializes an MCP session, lists its tools, and calls `add`.
- `requirements.txt` lists the Python dependency.

Both programs emit operational logs to stderr. This is important for the server: its stdout is reserved for MCP JSON-RPC messages when using the stdio transport.
