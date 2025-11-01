from fastapi import FastAPI
from playgen import generate_playcall  # dein Modul

app = FastAPI()

@app.get("/random_play")
def random_play():
    play = generate_playcall()
    return {"playcall": play}