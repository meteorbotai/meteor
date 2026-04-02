#!/usr/bin/env bash
# curl -fsSL https://raw.githubusercontent.com/yourusername/meteor/main/setup.sh | bash
set -euo pipefail

REPO="https://github.com/yourusername/meteor"
DIR="$HOME/meteor"

echo "==> Installing Bun..."
curl -fsSL https://bun.sh/install | bash
export BUN_INSTALL="$HOME/.bun"
export PATH="$BUN_INSTALL/bin:$PATH"

echo "==> Installing system dependencies..."
sudo apt-get update -qq && sudo apt-get install -y git unzip

echo "==> Installing uv..."
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"

echo "==> Installing Claude Code and pm2..."
bun install -g @anthropic-ai/claude-code pm2

echo "==> Cloning Meteor..."
git clone "$REPO" "$DIR"

echo "==> Installing Python dependencies (uv sync)..."
cd "$DIR" && uv sync

echo "==> Creating data and workspace directories..."
mkdir -p "$DIR/data" "$DIR/workspace"

echo ""
echo "Done! Next steps:"
echo ""
echo "  cd $DIR"
echo "  cp .env.example .env"
echo "  nano .env          # fill in your API keys"
echo "  bun run start"
echo ""
