from pydantic import BaseModel
from typing import List, Dict, Optional

class Observation(BaseModel):
    """What the agent sees at each step."""
    conversation: List[Dict[str, str]]
    step_count: int
    current_customer_query: str

class Action(BaseModel):
    """The action the agent takes (must be a response string)."""
    response: str

class State(BaseModel):
    """The internal state for the state() method required by OpenEnv."""
    current_task_index: int
    step_count: int
    is_done: bool
