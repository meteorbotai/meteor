import pty

from dotenv import load_dotenv

from constants import ENV_PATH, MCP_CONFIG_PATH

load_dotenv(ENV_PATH)

cmd = [
    "claude",
    "--mcp-config",
    str(MCP_CONFIG_PATH),
]


def chat() -> None:
    pty.spawn(cmd)


if __name__ == "__main__":
    chat()
