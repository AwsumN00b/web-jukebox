from fastapi import FastAPI
from pydantic import BaseModel, Field
import uvicorn
import threading
import Jukebox


jkbox = Jukebox.Jukebox()

app = FastAPI(
        title="Jukebox API"
        )

def runJukebox():
    global jkbox

    jkbox.autoplay()


class RequestItem(BaseModel):
    from_: str = Field(None,  alias="song", example="Darude Sandstorm")

@app.post("/songrequest")
async def addSongToQueue(item: RequestItem):
    global jkbox

    jkbox.add(RequestItem.from_)

    return "test-addSongToQueue"


@app.get("/pauseplay")
async def pausePlay():
    # make player stop or start

    return "test-pausePlay"


@app.get("/skip")
async def skip():
    # Skip current song, play next one

    return "test-skip"


def main():
    musicplayer = threading.Thread(name="jukebox", target=runJukebox)

    uvicorn.run("main:app", host="0.0.0.0", port=2112, log_level="info", reload=True)

if __name__ == "__main__":
    main()
