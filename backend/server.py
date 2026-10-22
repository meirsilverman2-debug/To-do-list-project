import os

from backend.routes.tasks_route import tasks_bp
from backend.routes.users_route import soldiers_bp
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS
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



@app.errorhandler(HTTPException)
def HttpErrors(e: HTTPException):
    response = jsonify({
        "code": e.code,
        "name": e.name,
        "description": e.description
    })
    return response, e.code

@app.errorhandler(Exception)
def unexpected_error(e: Exception):
    print(str(e))
    response = jsonify({
        "code": 500,
        "name": "Internal server error",
        "description": "something went wrong, try again later"
    })
    return response, 500
    



@app.route("/health", methods=["GET"])
def health():
    return jsonify({"message": "Server is on"}), 200

app.register_blueprint(soldiers_bp, url_prefix="/soldiers")
app.register_blueprint(tasks_bp, url_prefix="/tasks")




if __name__ == "__main__":
    app.run(port=int(os.getenv("PORT", 3000)))
