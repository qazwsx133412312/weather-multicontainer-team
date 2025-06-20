from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/')
def data():
    return jsonify({
        "city": "Kyiv",
        "temperature": round(random.uniform(10, 30), 1),
        "sky": random.choice(["Sunny", "Cloudy", "Rainy"]),
        "pressure": round(random.uniform(1000, 1025), 1)
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

