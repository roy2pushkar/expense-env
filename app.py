from fastapi import FastAPI
from environment import ExpenseEnv

app = FastAPI()

env = ExpenseEnv()

@app.post("/reset")
def reset():
    return {
        "state": env.reset()
    }

@app.post("/step")
def step(action: str):
    state, reward, done = env.step(action)
    return {
        "state": state,
        "reward": reward,
        "done": done
    }

@app.get("/state")
def state():
    return {
        "state": env.state()
    }