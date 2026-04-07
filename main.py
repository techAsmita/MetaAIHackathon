from fastapi import FastAPI, HTTPException
from inference import CustomerSupportEnv
from env.models import Action, Observation, State

# Initialize the API and the Environment
app = FastAPI(title="OpenEnv Customer Support Simulator")
env = CustomerSupportEnv()

@app.post("/reset", response_model=Observation)
def reset(task_id: int = 0):
    """Resets the environment to a specific task."""
    try:
        return env.reset(task_index=task_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/step")
def step(action: Action):
    """Processes an agent's response and returns (obs, reward, done)."""
    try:
        # Standard OpenEnv return format
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
    """Returns the internal state for monitoring."""
    return env.state()

@app.get("/")
def health_check():
    """Simple check to see if the server is live."""
    return {"status": "online", "env": "CustomerSupportEnv"}
