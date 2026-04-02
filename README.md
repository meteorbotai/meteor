# Meteor

Long-running AI agent powered by Claude Code.

## Setup

```bash
curl -fsSL https://raw.githubusercontent.com/meteorbotai/meteor/main/setup.sh | bash
source ~/.bashrc
cd ~/meteor
cp .env.example .env
nano .env
bun run start
```

## Usage

```bash
pm2 logs agent     # view logs
pm2 restart agent  # restart
pm2 stop agent     # stop
```

## Database

```bash
sqlite3 ~/meteor/data/memory.db "SELECT * FROM tasks"
sqlite3 ~/meteor/data/memory.db "SELECT * FROM memories"
```
