from fastapi import FastAPI
from playgen import generate_playcall

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/random_play")
def random_play():
    play = generate_playcall()
    return {"playcall": play}
