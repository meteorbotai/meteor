import subprocess
import time

from dotenv import load_dotenv

from constants import DELAY, MAX_TURNS, MCP_CONFIG_PATH, MISSION_PATH

load_dotenv()

cmd = [
    "claude",
    "-p",
    MISSION_PATH.read_text(),
    "--dangerously-skip-permissions",
    "--output-format",
    "stream-json",
    "--verbose",
    "--max-turns",
    str(MAX_TURNS),
    "--mcp-config",
    str(MCP_CONFIG_PATH),
]


def loop() -> None:
    while True:
        subprocess.run(cmd, stdin=subprocess.DEVNULL)
        time.sleep(DELAY)


if __name__ == "__main__":
    loop()
