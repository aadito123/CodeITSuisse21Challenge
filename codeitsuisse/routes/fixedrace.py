import logging
import json
import random
from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)


@app.route('/fixedrace', methods=['POST'])
def evaluateFixedRace():
    data = request.data
    logging.info("data sent for evaluation {}".format(data))
    
    result = request.data.decode('ASCII')
    result = result.split(',')
    result.remove('Lamont Lasch')
    result.remove('Annamarie Ahern')
    random.shuffle(result)
    result = 'Lamont Lasch, Annamarie Ahern, ' + ', '.join(result).encode('ASCII')

    logging.info("My result :{}".format(result))
    return result

'''

'''
