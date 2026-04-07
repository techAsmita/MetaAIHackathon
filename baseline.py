import random
import numpy as np
from openenv_env import OpenEnv  # your environment class

# Fix random seed for reproducibility
SEED = 42
random.seed(SEED)
np.random.seed(SEED)

# List of tasks
tasks = ["easy_task", "medium_task", "hard_task"]  # replace with your actual task names

# Run baseline for each task
for task_name in tasks:
    print(f"\nRunning baseline for task: {task_name}")
    
    env = OpenEnv(task=task_name)
    env.reset()
    
    done = False
    total_reward = 0.0
    steps = 0
    
    while not done:
        # Replace with your action space, here we choose random action
        action = env.sample_action()
        obs, reward, done, info = env.step(action)
        total_reward += reward
        steps += 1
    
    print(f"Task {task_name} completed in {steps} steps with total reward: {total_reward:.3f}")