from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
from werkzeug.exceptions import HTTPException

load_dotenv()


app = Flask(__name__)
CORS(
    app,
    resources={
        r"/*": {
            "origins": ["http://localhost:3000", "http://localhost:5173"],
            "supports_credentials": True,
        }
    },
)


@app.before_request
def logger():
    print(f"[REQ] {request.method}/{request.url}")
    print(f"body: {request.get_json(silent=True)} | query: {request.args.to_dict()}")


@app.errorhandler(Exception)
def error_format(error: Exception):
    print(str(error))
    status = error.code or 500
    message = str(error) or "Internal server error"
    return jsonify({"err": message}), status


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"message": "Server is on"}), 200




if __name__ == "__main__":
    app.run(port=int(os.getenv("PORT")))
