# StudyRewards :)

**StudyRewards** is a desktop productivity application built with **Python** and **PyQt6**. It gamifies your study sessions by turning focus time into a digital currency. Complete your tasks, finish Pomodoro cycles, and earn coins to spend on rewards that you define yourself!

---

## Features

### 1. Pomodoro Timer & Coin System
The core of the app is a focus timer designed to reward your persistence.
* **Earn While You Learn:** For every 25 minutes of work, you earn **5 coins**.
* **Dynamic Scaling:** The reward scales at 1 coin per 5 minutes (minimum session: 5 minutes).
* **Cycle Tracking:** The app automatically counts and saves your completed Pomodoro cycles.
* **Customizable:** Features customizable timer buttons to suit your workflow (Coming Soon).

### 2. Task Management
Stay organized and get paid for your effort.
* **Paid Tasks:** Add specific tasks and set their "bounty" (up to a **20-coin limit**).
* **Auto-Archive:** Once a task is crossed out, it moves to the "Done Today/This Week" archive and won't reappear on the next launch.
* **Progress Tracking:** Visual cues for completed tasks to keep you motivated.

### 3. Custom Rewards Store
You decide what your hard work is worth.
* **Personalized Shop:** Create your own rewards (e.g., *"30 mins of The Sims 4"* for 15 coins).
* **Guilt-Free Breaks:** Spend your hard-earned balance to "unlock" your relaxation time.

### 4. Data & Profiles
* **Coin Balance & Archive:** Track your current wallet and your total lifetime earnings.
* **Data Persistence:** All progress, tasks, and coins are saved automatically.
* **Multi-User Support:** (Planned) Profiles to allow different users to track their progress separately.

---

## Tech Stack

* **Language:** [Python](https://www.python.org/)
* **GUI Framework:** [PyQt6](https://pypi.org/project/PyQt6/)
* **Data Storage:** Local JSON

---

## Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/study_rewards.git](https://github.com/yourusername/study_rewards.git)
    cd study_rewards
    ```

2.  **Install dependencies:**
    ```bash
    pip install PyQt6
    ```

3.  **Run the application:**
    ```bash
    python main.py
    ```

---

## 📖 How it Works

1.  **Set Your Goals:** Add your daily tasks and assign them a coin value.
2.  **Focus:** Start the Pomodoro timer.
3.  **Collect:** Once the timer finishes or a task is checked off, your balance increases.
4.  **Redeem:** Go to your Rewards tab and spend your coins on a break!

---

*Made with ❤️ to stop procrastination. (mainly for myself, haha)*