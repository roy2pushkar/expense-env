import os
import requests

print("FILE EXECUTING NOW 🚀")

BASE_URL = os.getenv("API_BASE_URL", "http://127.0.0.1:8000")

def run_episode():
    print("Starting episode...")

    response = requests.post(f"{BASE_URL}/reset")
    print("Reset response:", response.text)

    state = response.json()
    total_reward = 0

    for i in range(10):
        action = "save"

        res = requests.post(f"{BASE_URL}/step", params={"action": action})
        print(f"Step {i} response:", res.text)

        data = res.json()

        state = data.get("state", data)
        reward = data["reward"]
        done = data["done"]

        total_reward += reward

        if done:
            break

    return state, total_reward


if __name__ == "__main__":
    print("Running inference...")

    final_state, total_reward = run_episode()

    print("Final State:", final_state)
    print("Total Reward:", total_reward)