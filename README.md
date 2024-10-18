# The Fake Incrementer - TFI

Welcome to TFI - The Fun Incrementer, a fun and interactive project that simulates fake earnings growth in real-time! Whether you want to pretend you're earning big or just enjoy watching numbers rise, this app is designed to give you that dopamine hit of success—without the actual cash! 🤑

## Features
- Dynamic Earnings: Watch your fake total earnings, reward earnings, and completed tasks increase smoothly.
- Payout Simulation: Payout values increase in sync with your earnings. Fake wealth, fake payouts! 💵
- Smooth Transitions: All updates happen with satisfying smooth transitions to make it feel like you're growing rich.
- Task Completion Counter: Completed tasks count goes up as you "earn" more!
- PayPal Logo: Features the PayPal logo to make it look like real payments are happening!

---

## How It Works ?
The app simulates earnings and payouts in real-time with automatic updates every few seconds. The following values are incremented:
- Total Earnings
- Reward Earnings
- Tasks Completed
- Payout Amount
All values increase smoothly with small random increments, simulating the look and feel of a real payment dashboard.

---

## Installation
To run this project locally, follow these simple steps:

- Clone the repository:
    ```
    git clone github.com/arktrek/TFI.git
    ```
- Navigate to the project directory:

    ```
    cd TFI
    ```
- Install dependencies:
    ```
    pip install flask
    ```
- Run the app:

    ```
    python app.py
    ```
- Open your browser and go to http://127.0.0.1:5000 to see your fake riches grow!

---
## Usage:
Once you've started the Flask app, the dashboard will automatically begin simulating:

- Total Earnings: Increments by a random value every 2 seconds.
- Reward Earnings: Follows a smaller incremental pattern.
- Tasks Completed: Incremented by 1 with each earning update.
- Payouts: Automatically synced with total earnings to provide realistic payout values.
Just sit back and watch your imaginary bank account fill up!

--- 

## Technologies Used:
- Flask: Backend framework to serve the dashboard.
- JavaScript: Handles real-time updates and smooth transitions.
- HTML & CSS: Provides the structure and styling for the UI.
- PayPal Logo: Directly sourced from PayPal to add that extra bit of realism!

