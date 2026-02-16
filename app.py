from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return "Hello from Flask (Docker + GitHub Actions)!"

@app.get("/health")
def health():
    return jsonify(status="ok")

if __name__ == "_main_":
    app.run(host="0.0.0.0", port=5000)