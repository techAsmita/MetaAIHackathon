import os
import requests
import sys

# Requirements for Phase 2 Validation
API_BASE_URL = os.getenv("API_BASE_URL", "http://0.0.0")
MODEL_NAME = os.getenv("MODEL_NAME", "metaai-support-agent")
HF_TOKEN = os.getenv("HF_TOKEN")

def run_baseline():
    # Loop through your 3 tasks
    for task_id in range(3):
        task_name = f"Task_{task_id}"
        
        # 1. [START] Block
        print(f"[START] task={task_name}", flush=True)
        
        try:
            # Reset
            resp = requests.post(f"{API_BASE_URL}/reset", params={"task_id": task_id})
            obs = resp.json()
            
            # Action (Generic for baseline)
            action = {"response": "I am very sorry for the trouble. I will help you with this right now."}
            
            # Step
            step_resp = requests.post(f"{API_BASE_URL}/step", json=action)
            result = step_resp.json()
            
            reward = float(result.get("reward", 0.0))
            
            # 2. [STEP] Block (The validator needs to see this for every step)
            print(f"[STEP] step=1 reward={reward}", flush=True)
            
            # 3. [END] Block (Final summary for this task)
            print(f"[END] task={task_name} score={reward} steps=1", flush=True)
            
        except Exception as e:
            # If it fails, still print an END block with 0 to avoid hanging the validator
            print(f"[END] task={task_name} score=0.0 steps=0", flush=True)
            continue

if __name__ == "__main__":
    run_baseline()
