# check_output.py
from inference import CustomerSupportEnv
from env.models import Action  

env = CustomerSupportEnv()

# Test Task 0 (Refund)
obs = env.reset(task_index=0)
action = Action(response="I am sorry, I will process your refund.")
obs, reward, done, _ = env.step(action)

print(f"Task: {obs.current_customer_query}")
print(f"Reward: {reward}") # Should be 1.0
print(f"Done: {done}")