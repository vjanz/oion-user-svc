import os
from flask import Flask, jsonify
from custom_exceptions import APIException
from utils import read_json, generate_json_response

app = Flask(__name__)
with app.app_context():
    # within this block, current_app points to app.
    users = read_json('users.json')
    users_json = generate_json_response(users)


@app.errorhandler(APIException)
def handle_api_exception(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.route("/")
def get_root():
    return {"message": f"Hello from oion-user-service application [env:{os.getenv('ENVIRONMENT')}]"}


@app.route("/users", methods=['GET'])
def get_users():
    if not users:
        raise APIException(message="Users not found", status_code=404)
    return users_json

