import json
import requests
from flask import jsonify


def read_json(file_name: str):
    with open(file_name, "r") as read_file:
        json_loaded = json.load(read_file)
        return json_loaded


def generate_json_response(data):
    if not data:
        raise Exception("Data is Empty")
    return jsonify(data)


def fetch_from_url(url: str):
    if not url:
        raise Exception("Url is null")
    r = requests.get(url)
    if r.status_code > 400:
        return f"Couldn't fetch the data from {url}"
    return r.json()



