from flask import Flask, request
import json, os, logging
from datetime import datetime

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route("/webhook", methods=["POST"])
def telegram_webhook():
    data = request.get_json(force=True)
    logging.info("=== NEW UPDATE ===")
    logging.info(json.dumps(data, indent=2, ensure_ascii=False))
    return "OK", 200

@app.route("/", methods=["GET"])
def index():
    return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
