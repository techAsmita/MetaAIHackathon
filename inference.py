from typing import List, Dict, Tuple
from env.models import Observation, Action 

class CustomerSupportEnv:
    def __init__(self):
        self.tasks = [
            {"id": 0, "name": "Easy_Refund", "query": "I want a refund", "key": "refund"},
            {"id": 1, "name": "Medium_Frustration", "query": "I am frustrated", "key": "apologize"},
            {"id": 2, "name": "Hard_Escalation", "query": "I want to escalate", "key": "manager"}
        ]
        self.started = False  #  fix duplicate START
        self.reset()

    def reset(self, task_index: int = 0) -> Observation:
        self.history = []
        self.step_count = 0
        self.current_task_index = task_index % len(self.tasks)
        task = self.tasks[self.current_task_index]
        self.current_query = task["query"]

        #  PRINT START ONLY ONCE
        if not self.started:
            print(f"[START] task={task['name']}", flush=True)
            self.started = True

        return self.get_observation()

    def step(self, action: Action) -> Tuple[Observation, float, bool, Dict]:
        response_text = action.response
        self.history.append({"agent": response_text, "customer": self.current_query})
        self.step_count += 1

        reward = float(self.compute_reward(response_text))
        done = True 

        print(f"[STEP] step={self.step_count} reward={reward}", flush=True)

        if done:
            task_name = self.tasks[self.current_task_index]["name"]
            print(f"[END] task={task_name} score={reward} steps={self.step_count}", flush=True)

            #  RESET FLAG FOR NEXT TASK
            self.started = False

        return self.get_observation(), reward, done, {}

    def get_observation(self) -> Observation:
        return Observation(
            conversation=self.history,
            step_count=self.step_count,
            current_customer_query=self.current_query
        )

    def state(self):
        return {
            "current_task_index": self.current_task_index,
            "step_count": self.step_count,
            "is_done": self.step_count > 0
        }

    def compute_reward(self, response: str) -> float:
        score = 0.0
        r = response.lower()
        task = self.tasks[self.current_task_index]

        if any(word in r for word in ["sorry", "apologize", "understand"]):
            score += 0.3

        if task["key"] in r:
            score += 0.7

        return min(score, 1.0)
