from flask import Flask
import redis
import os

app = Flask(__name__)

# Connect to Redis
r = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=6379,
    decode_responses=True
)

# Route 1: Welcome message
@app.route("/")
def home():
    return "Welcome to the Flask and Redis application!"

# Route 2: Increment and display visit count
@app.route("/count")
def visit_count():
    count = r.incr("visit_count")
    return f"This page has been visited {count} times."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)