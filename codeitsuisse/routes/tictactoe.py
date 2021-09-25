import logging
import json
import requests
from flask import request, jsonify
#from flask_sse import sse

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/tic-tac-toe', methods=['POST'])
def evaluateTicTacToe():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    battleId = data.get("battleId")
    result = 0
    got = requests.get('https://cis2021-arena.herokuapp.com/tic-tac-toe/' + battleId)
    logging.info("got: {}".format(got.text))
    logging.info("My result :{}".format(result))
    return json.dumps(result)
