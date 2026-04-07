from typing import List, Dict, Tuple
from env.models import Observation, Action 

class CustomerSupportEnv:
    def __init__(self):
        # 3 tasks with unique 'keys' to ensure score variance across difficulties
        self.tasks = [
            {"id": 0, "name": "Easy Refund", "query": "I want a refund", "key": "refund"},
            {"name": "Medium Frustration", "query": "I am frustrated", "key": "apologize"},
            {"name": "Hard Escalation", "query": "I want to escalate", "key": "manager"}
        ]
        self.reset()

    def reset(self, task_index: int = 0) -> Observation:
        """Standard OpenEnv reset: cleans state and sets the task."""
        self.history: List[Dict[str, str]] = []
        self.step_count: int = 0
        self.current_task_index: int = task_index % len(self.tasks)
        self.current_query: str = self.tasks[self.current_task_index]["query"]
        return self.get_observation()

    def step(self, action: Action) -> Tuple[Observation, float, bool, Dict]:
        """Standard OpenEnv step: processes action and returns (obs, reward, done, info)."""
        # action is now the Pydantic model we defined
        response_text = action.response
        
        self.history.append({
            "agent": response_text,
            "customer": self.current_query
        })
        self.step_count += 1

        # Calculate shaped reward (0.0 to 1.0)
        reward = self.compute_reward(response_text)
        
        # In this simulator, one response completes the task
        done = True 
        
        return self.get_observation(), float(reward), done, {}

    def get_observation(self) -> Observation:
        """Helper to return the typed Observation model."""
        return Observation(
            conversation=self.history,
            step_count=self.step_count,
            current_customer_query=self.current_query
        )

    def state(self):
        """Standard OpenEnv state method."""
        return {
            "current_task_index": self.current_task_index,
            "step_count": self.step_count,
            "is_done": self.step_count > 0
        }

    def compute_reward(self, response: str) -> float:
        """Deterministic grader with variable signal (Phase 2 requirement)."""
        score = 0.0
        r = response.lower()
        task = self.tasks[self.current_task_index]

        # 1. Base Professionalism (partial reward)
        if any(word in r for word in ["sorry", "apologize", "understand"]):
            score += 0.3
        
        # 2. Task Accuracy (weighted signal)
        if task["key"] in r:
            score += 0.7
            
        return min(score, 1.0)
