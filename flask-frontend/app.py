import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get("http://express-service:5000/api")
    return f"<h1>Flask Frontend</h1><p>Backend says: {response.text}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
