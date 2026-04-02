# Meteor — Mission

## Long-Term Goal

[Describe your agent's purpose here. This is the one thing that never changes.
Be specific about what success looks like over the long run.]

## Behavioral Rules

- At the start of every session, query the `tasks` table for pending or in-progress work.
- Pick the highest-priority pending task and work on it until it is done or blocked.
- When a task is complete, update its `status` to `done` and write a short `outcome`.
- When genuinely stuck or needing a decision, use the Telegram MCP tool to ask me directly and wait for my reply before proceeding.
- Store anything worth remembering long-term (patterns, credentials locations, learnings) as a row in the `memories` table.
- If no tasks exist or if all tasks have been completed, brainstorm the next best steps and add them to the queue.
- Never modify this file (CLAUDE.md).

## Memory — SQLite Database

The database lives at `data/memory.db`. Use the `sqlite-memory` MCP tool to query and write.

### tasks

| column      | type    | notes                                       |
| ----------- | ------- | ------------------------------------------- |
| id          | INTEGER | primary key                                 |
| created_at  | INTEGER | unix timestamp                              |
| updated_at  | INTEGER | unix timestamp                              |
| title       | TEXT    | short name for the task                     |
| status      | TEXT    | `pending`, `in_progress`, `done`, `blocked` |
| description | TEXT    | full details                                |
| outcome     | TEXT    | filled in when done or blocked              |

### memories

| column     | type    | notes          |
| ---------- | ------- | -------------- |
| id         | INTEGER | primary key    |
| created_at | INTEGER | unix timestamp |
| content    | TEXT    | the memory     |
