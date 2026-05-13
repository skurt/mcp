import sys
from pathlib import Path
from mcp.server.fastmcp import FastMCP

ROOT = Path(__file__).parent
PROMPTS_DIR = ROOT / "prompts"

mcp = FastMCP("prompt-library", host="0.0.0.0", port=8000)

# Lists all prompts available in the MCP server.
@mcp.tool(
    name="list_prompt_files",
    description="List all available prompt files."
)
def list_prompt_files() -> list[str]:
    print("Tool called: list_prompt_files", file=sys.stderr, flush=True)
    return [p.name for p in PROMPTS_DIR.iterdir() if p.is_file()]

# Retrieves the contents of the specific file.
# Expects a literal path to the file in this version.
@mcp.tool(
    name="get_prompt_file",
    description="Retrieve the contents of a prompt file by name."
)
def get_prompt_file(name: str) -> str:
    print(f"Tool called: get_prompt_file(name={name!r})", file=sys.stderr, flush=True)
    path = PROMPTS_DIR / name
    if not path.exists():
        raise FileNotFoundError(name)
    return path.read_text(encoding="utf-8")

if __name__ == "__main__":
    print("MCP server 'prompt-library' is running.", file=sys.stderr, flush=True)
    mcp.run(transport="streamable-http")