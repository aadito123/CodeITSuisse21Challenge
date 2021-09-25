import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

def guessPassword(possible, num_slots, history):
    pass

@app.route('/decoder', methods=['POST'])
def evaluateDecoder():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    possible = data['possible_values']
    num_slots = data['num_slots']
    history = data['history']

    result = guessPassword(possible, num_slots, history)
    logging.info("My result :{}".format(result))
    return json.dumps(result)
