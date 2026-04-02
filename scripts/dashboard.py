"""JSON at /, SSE log at /log."""

import asyncio
import os
import sqlite3

from fastapi import FastAPI
from fastapi.responses import StreamingResponse

from constants import DATA_DIR, DB_PATH, LOG_PATH

app = FastAPI(docs_url=None, redoc_url=None)

_SSE = {
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "X-Accel-Buffering": "no",
}


@app.get("/")
def root():
    if not DB_PATH.exists():
        return {"tasks": [], "memories": []}
    with sqlite3.connect(DB_PATH) as c:
        c.row_factory = lambda cur, row: dict(
            zip([col[0] for col in cur.description], row)
        )
        tasks = c.execute("SELECT * FROM tasks ORDER BY updated_at DESC").fetchall()
        mems = c.execute("SELECT * FROM memories ORDER BY created_at DESC").fetchall()
    return {"tasks": tasks, "memories": mems}


async def stream_log():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    LOG_PATH.touch(exist_ok=True)
    with open(LOG_PATH) as f:
        f.seek(0, 2)
        while True:
            line = f.readline()
            if line:
                yield f"data: {line.rstrip()}\n\n"
            else:
                await asyncio.sleep(0.25)


@app.get("/log")
def log_stream():
    return StreamingResponse(stream_log(), media_type="text/event-stream", headers=_SSE)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", "8080")))
