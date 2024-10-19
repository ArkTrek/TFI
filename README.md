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

1. Clone the repository:
    ```
    git clone github.com/arktrek/TFI.git
    ```
2. Navigate to the project directory:

    ```
    cd TFI
    ```
3. Install dependencies:
    ```
    pip install flask
    ```
4. Run the app:

    ```
    python app.py
    ```
5. Open your browser and go to http://127.0.0.1:5000 to see your fake riches grow!

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

---

## Customization
### Adjust Increment Speed:
   Want to increase or decrease how fast your fake earnings grow? Modify the setInterval function in the JavaScript code:
   ```
        setInterval(updateEarnings, 2000);  // Updates every 2 seconds
   ```
    
   ---
    
   ### Change Increment Amounts
   To earn faster, you can modify the random increment values for earnings:
   ```
        let newTotalEarnings = totalEarnings + (Math.random() * 1);
        let newRewardEarnings = rewardEarnings + (Math.random() * 0.2);
   ```
    
   ---
    
   ### Replace the PayPal Logo
   If you prefer another payment provider logo (or your own fictional one), just replace the PayPal image URL:
   ```
            <img src="https://www.paypalobjects.com/webstatic/mktg/logo/pp_cc_mark_111x69.jpg" alt="PayPal" class="paypal-logo">
   ```
        
   --- 
    
   ### Contributing
   Feel free to submit issues or pull requests to make TFI - The Fun Incrementer even more fun! 🎉 Contributions are always welcome, and you can:
    
   - Add new features like custom earning types.
   - Improve the UI to make it even more engaging.
   - Create new animations for earning updates.
    
   ---
    
   ### License
   This project is licensed under the GNU General Public License. Enjoy it, modify it, and share it—just don't take the numbers too seriously! 😄
