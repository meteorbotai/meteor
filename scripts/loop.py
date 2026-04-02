import subprocess
import time

from constants import DATA_DIR, DELAY, LOG_PATH, MAX_TURNS, MCP_CONFIG_PATH, MISSION_PATH

DATA_DIR.mkdir(parents=True, exist_ok=True)

log = open(LOG_PATH, "a", buffering=1)

while True:
    cmd = [
        "claude",
        "-p",
        MISSION_PATH.read_text(),
        "--dangerously-skip-permissions",
        "--output-format",
        "stream-json",
        "--max-turns",
        str(MAX_TURNS),
        "--mcp-config",
        str(MCP_CONFIG_PATH),
    ]
    subprocess.run(cmd, stdout=log, stderr=log)
    time.sleep(DELAY)
