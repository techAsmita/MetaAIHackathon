import os

# STOP THIS FILE DURING EVALUATION
if os.getenv("RUN_ENV") == "runner":
    exit()

from fastapi import FastAPI, HTTPException
from inference import CustomerSupportEnv
from env.models import Action, Observation, State

app = FastAPI(title="OpenEnv Customer Support Simulator")
env = CustomerSupportEnv()

@app.post("/reset", response_model=Observation)
def reset(task_id: int = 0):
    try:
        return env.reset(task_index=task_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/step")
def step(action: Action):
    try:
        obs, reward, done, info = env.step(action)
        return {
            "observation": obs,
            "reward": float(reward),
            "done": done,
            "info": info
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/state")
def get_state():
    return env.state()

@app.get("/")
def health_check():
    return {"status": "online", "env": "CustomerSupportEnv"}
