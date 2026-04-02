from pathlib import Path

ROOT = Path(__file__).parent

ENV_PATH = ROOT / ".env"
MCP_CONFIG_PATH = ROOT / ".mcp.json"
MISSION_PATH = ROOT / "CLAUDE.md"

WORKSPACE_DIR = ROOT / "workspace"
DB_PATH = WORKSPACE_DIR / "memory.db"

DELAY = 30
MAX_TURNS = 500
