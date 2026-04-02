import subprocess

from dotenv import load_dotenv

from constants import MCP_CONFIG_PATH

load_dotenv()

cmd = [
    "claude",
    "--dangerously-skip-permissions",
    "--mcp-config",
    str(MCP_CONFIG_PATH),
]


def chat() -> None:
    subprocess.run(cmd)


if __name__ == "__main__":
    chat()
