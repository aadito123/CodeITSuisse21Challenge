import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)


@app.route('/fixedrace', methods=['POST'])
def evaluateFixedRace():
    data = request.data
    logging.info("data sent for evaluation {}".format(data))
    
    result = request.data
    logging.info("My result :{}".format(result))
    return result
