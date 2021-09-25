import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)


@app.route('/fixedrace', methods=['POST'])
def evaluateFixedRace():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    
    result = 0
    logging.info("My result :{}".format(result))
    return json.dumps(result)