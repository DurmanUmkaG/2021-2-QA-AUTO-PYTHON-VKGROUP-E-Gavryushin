import json
import threading

from flask import Flask, request, jsonify

import settings

app = Flask(__name__)

SURNAME_DATA = {}


@app.route('/add_user', methods=['POST'])
def add_user():
    data = json.loads(request.data)
    user_name = data['name']
    user_surname = data['surname']
    if user_name not in SURNAME_DATA:
        SURNAME_DATA[user_name] = user_surname
        return jsonify(SURNAME_DATA), 201
    else:
        return jsonify(f'User name {user_name} already exists: surname: {user_surname}'), 400


@app.route('/get_surname/<name>', methods=['GET'])
def get_user_surname(name):
    if surname := SURNAME_DATA.get(name):
        return jsonify(surname), 200
    else:
        return jsonify(f'Surname for user "{name}" not found'), 404


def run_mock():
    server = threading.Thread(target=app.run, kwargs={
        'host': settings.MOCK_HOST,
        'port': settings.MOCK_PORT,
    })
    server.start()

    return server


def shutdown_mock():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


@app.route('/shutdown', methods=['GET'])
def shutdown():
    shutdown_mock()
    return jsonify(f'Ok, exiting'), 200
