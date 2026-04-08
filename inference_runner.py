from inference import CustomerSupportEnv

class Action:
    def __init__(self, response):
        self.response = response


def run_baseline():
    env = CustomerSupportEnv()

    tasks = ["Easy_Refund", "Medium_Frustration", "Hard_Escalation"]

    for task_id, task_name in enumerate(tasks):
        try:
            obs = env.reset(task_index=task_id)

            if task_name == "Easy_Refund":
                response = "I understand your issue and will process your refund immediately."
            elif task_name == "Medium_Frustration":
                response = "I am really sorry and I understand your frustration."
            else:
                response = "I understand your concern and will connect you to a manager right away."

            action = Action(response=response)

            obs, reward, done, _ = env.step(action)

        except Exception:
            print(f"[END] task={task_name} score=0.0 steps=0", flush=True)


if __name__ == "__main__":
    run_baseline()
