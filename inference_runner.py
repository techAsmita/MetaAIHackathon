import os
import requests


API_BASE_URL = os.getenv("API_BASE_URL", "http://0.0.0")
MODEL_NAME = os.getenv("MODEL_NAME", "meta-ai-support-baseline")


HF_TOKEN = os.getenv("HF_TOKEN")

def run_baseline():
    print(f"Running Meta AI OpenEnv Baseline using model: {MODEL_NAME}...")
    
    # Range(3) covers task IDs 0, 1, and 2
    for task_id in range(3):
        try:
            # 1. Reset for specific task
            # Using API_BASE_URL instead of hardcoded local IP
            response = requests.post(f"{API_BASE_URL}/reset", params={"task_id": task_id})
            response.raise_for_status()
            obs = response.json()
            
            print(f"\n--- Task {task_id} ---")
            print(f"Customer Query: {obs['current_customer_query']}")
            
            # 2. Step with a polite agent response
            action = {"response": "I am very sorry for the trouble. I will help you with this right now."}
            step_response = requests.post(f"{API_BASE_URL}/step", json=action)
            step_response.raise_for_status()
            result = step_response.json()
            
            # Extract reward
            reward = result.get("reward", 0.0)
            print(f"Agent Response: {action['response']}")
            print(f"Reward Received: {reward}")
            print(f"Status: {'Success' if reward > 0 else 'Failed'}")
        
        except Exception as e:
            print(f"Error on Task {task_id}: {e}")
            print("Ensure your environment API is accessible via API_BASE_URL.")

if __name__ == "__main__":
    run_baseline()
