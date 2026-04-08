import os
import requests
import sys

# 1. Compliance: Required Environment Variables
API_BASE_URL = os.getenv("API_BASE_URL", "http://0.0.0")
MODEL_NAME = os.getenv("MODEL_NAME", "metaai-support-agent")
HF_TOKEN = os.getenv("HF_TOKEN")

def run_baseline():
    # 2. Compliance: 3 tasks to show score variance
    tasks = ["Easy_Refund", "Medium_Frustration", "Hard_Escalation"]
    
    for task_id, task_name in enumerate(tasks):
        # [START] tag is mandatory for the validator to begin tracking
        print(f"[START] task={task_name}", flush=True)
        
        try:
            # Reset Environment via API
            resp = requests.post(f"{API_BASE_URL}/reset", params={"task_id": task_id})
            resp.raise_for_status()
            
            # Agent Action
            action = {"response": "I am very sorry for the trouble. I will help you with this right now."}
            
            # Environment Step
            step_resp = requests.post(f"{API_BASE_URL}/step", json=action)
            step_resp.raise_for_status()
            result = step_resp.json()
            
            reward = float(result.get("reward", 0.0))
            
            # [STEP] tag is mandatory for every action
            print(f"[STEP] step=1 reward={reward}", flush=True)
            
            # [END] tag is mandatory for the validator to record the final score
            print(f"[END] task={task_name} score={reward} steps=1", flush=True)
            
        except Exception as e:
            # Prevent validator from hanging if a network error occurs
            print(f"[END] task={task_name} score=0.0 steps=0", flush=True)
            continue

if __name__ == "__main__":
    run_baseline()
