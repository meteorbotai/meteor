from pathlib import Path

ROOT = Path(__file__).parent.parent

MCP_CONFIG_PATH = ROOT / ".mcp.json"
MISSION_PATH = ROOT / "CLAUDE.md"

DATA_DIR = ROOT / "data"
DB_PATH = DATA_DIR / "memory.db"
LOG_PATH = DATA_DIR / "agent.log"

DELAY = 30
MAX_TURNS = 500
