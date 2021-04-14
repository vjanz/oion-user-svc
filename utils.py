import json

from flask import jsonify


def read_json(file_name: str):
    with open(file_name, "r") as read_file:
        json_loaded = json.load(read_file)
        return json_loaded


def generate_json_response(data):
    if not data:
        raise Exception("Data is Empty")
    return jsonify(data)
