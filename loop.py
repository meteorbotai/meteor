import subprocess
import time

from constants import DELAY, MAX_TURNS, MCP_CONFIG_PATH, MISSION_PATH

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


def loop() -> None:
    while True:
        subprocess.run(cmd)
        time.sleep(DELAY)


if __name__ == "__main__":
    loop()
