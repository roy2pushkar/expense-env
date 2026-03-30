class ExpenseEnv:
    def __init__(self):
        self.balance = 1000
        self.savings = 0
        self.step_count = 0

    def reset(self):
        self.balance = 1000
        self.savings = 0
        self.step_count = 0

        return self.state()

    def state(self):
        return {
            "balance": self.balance,
            "savings": self.savings,
            "step": self.step_count
        }

    def step(self, action):
        self.step_count += 1

        if action == "spend":
            self.balance -= 100
            reward = 0.1

        elif action == "save":
            self.savings += 100
            self.balance -= 100
            reward = 0.5

        elif action == "invest":
            self.savings += 150
            self.balance -= 100
            reward = 0.8

        else:
            reward = 0.0

        done = self.balance <= 0 or self.step_count >= 10

        return self.state(), reward, done