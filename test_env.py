# test_env.py
from inference import CustomerSupportEnv

env = CustomerSupportEnv()
obs = env.reset()
print("=== RESET ENV ===")
print(f"conversation={obs.conversation} step_count={obs.step_count} current_customer_query='{obs.current_customer_query}'")

for i in range(3):
    action = ""
    query = obs.current_customer_query
    if "refund" in query:
        action = "Sorry, we will refund your order"
    elif "frustrated" in query:
        action = "We understand, and we apologize for the trouble"
    elif "escalate" in query:
        action = "We will escalate this to our manager"

    obs, reward = env.step(action)[:2]
    print(f"\n=== STEP {i+1} ===")
    print(f"State: conversation={obs.conversation} step_count={obs.step_count} current_customer_query='{obs.current_customer_query}'")
    print(f"Reward: {reward}")