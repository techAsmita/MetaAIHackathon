from env.tasks import tasks
import random
from env.grader import grade

class SupportEnv:

    def __init__(self):
        self.state = None

    def reset(self):
        task = random.choice(tasks)
        self.state = task["input"]
        return {"query": self.state}

    def step(self, action):
        response = action["response"]
        score = grade(response)

        done = True
        return {"query": self.state}, score, done, {}