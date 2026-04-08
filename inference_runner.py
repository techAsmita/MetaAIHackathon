import os
import requests
import sys

# Required Environment Variables
API_BASE_URL = os.getenv("API_BASE_URL", "http://0.0.0")
MODEL_NAME = os.getenv("MODEL_NAME", "meta-ai-support-baseline")
HF_TOKEN = os.getenv("HF_TOKEN")

def run_baseline():
    # Loop through the 3 mandatory tasks
    tasks = ["Easy_Refund", "Medium_Frustration", "Hard_Escalation"]
    
    for task_id, task_name in enumerate(tasks):
        # 1. [START] Block - Must be first
        print(f"[START] task={task_name}", flush=True)
        
        try:
            # Reset Environment
            reset_resp = requests.post(f"{API_BASE_URL}/reset", params={"task_id": task_id})
            reset_resp.raise_for_status()
            
            # Baseline Action
            action = {"response": "I am very sorry for the trouble. I will help you with this right now."}
            
            # Step Environment
            step_resp = requests.post(f"{API_BASE_URL}/step", json=action)
            step_resp.raise_for_status()
            result = step_resp.json()
            
            reward = float(result.get("reward", 0.0))
            
            # 2. [STEP] Block - Must include step number and reward
            print(f"[STEP] step=1 reward={reward}", flush=True)
            
            # 3. [END] Block - Must include final score and total steps
            print(f"[END] task={task_name} score={reward} steps=1", flush=True)
            
        except Exception as e:
            # Error fallback to prevent the validator from hanging
            print(f"[END] task={task_name} score=0.0 steps=0", flush=True)
            continue

if __name__ == "__main__":
    run_baseline()
