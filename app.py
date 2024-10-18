from flask import Flask, render_template, jsonify
import time
import threading

app = Flask(__name__)

# Fake earnings variable
earnings = {"amount": 0}

# Function to simulate increasing earnings
def increase_earnings():
    while True:
        time.sleep(1)  # Delay in seconds between increments
        earnings["amount"] += 5  # Increment earnings by 5 every second

# Start the earnings incrementation in a background thread
thread = threading.Thread(target=increase_earnings)
thread.daemon = True  # Daemon thread will exit when the app does
thread.start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_earnings')
def get_earnings():
    return jsonify(earnings)

if __name__ == "__main__":
    app.run(debug=True)
