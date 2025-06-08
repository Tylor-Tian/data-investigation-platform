from flask import Flask, jsonify
from .api.investigations import investigations_bp

app = Flask(__name__)

app.register_blueprint(investigations_bp, url_prefix="/api/v1")

@app.route("/health")
def health_check():
    return jsonify(status="ok")
