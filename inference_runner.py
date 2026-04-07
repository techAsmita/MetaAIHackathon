import requests

# Hardcoded for local testing on Mac
BASE_URL = "http://127.0.0.1:8000"

def run_baseline():
    print("Running Meta AI OpenEnv Baseline...")
    
    # Range(3) covers task IDs 0, 1, and 2
    for task_id in range(3):
        try:
            # 1. Reset for specific task - Using params for FastAPI compatibility
            response = requests.post(f"{BASE_URL}/reset", params={"task_id": task_id})
            response.raise_for_status()
            obs = response.json()
            print(f"\n--- Task {task_id} ---")
            print(f"Customer Query: {obs['current_customer_query']}")
            
            # 2. Step with a polite agent response
            action = {"response": "I am very sorry for the trouble. I will help you with this right now."}
            step_response = requests.post(f"{BASE_URL}/step", json=action)
            step_response.raise_for_status()
            result = step_response.json()
            
            # Extract reward from the dictionary returned by main.py
            reward = result.get("reward", 0.0)
            print(f"Agent Response: {action['response']}")
            print(f"Reward Received: {reward}")
            print(f"Status: {'Success' if reward > 0 else 'Failed'}")
        
        except Exception as e:
            print(f"Error on Task {task_id}: {e}")
            print("Make sure your uvicorn server is running in another terminal!")

if __name__ == "__main__":
    run_baseline()
