import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)


@app.route('/parasite', methods=['POST'])
def evaluateParasite():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    inputValue = data.get("input")
    result = inputValue * inputValue
    logging.info("My result :{}".format(result))
    return json.dumps(result)
'''
Sample Input
[
  {
    "room": 1,
    "grid": [
      [0, 3],
      [0, 1]
    ],
    "interestedIndividuals": [
      "0,0"
    ]
  },
  {
    "room": 2,
    "grid": [
      [0, 3, 2],
      [0, 1, 1],
      [1, 0, 0]
    ],
    "interestedIndividuals": [
      "0,2", "2,0", "1,2"
    ]
  }
]
Output format
An object with the following parameters will be returned as response:

room: int
p1: dict { tuple [ int, int ]: int }
p2: int
p3: int
p4: int
Sample Output
[
  {
    "room": 1,
    "p1": { "0,0": -1},
    "p2": 1,
    "p3": 1,
    "p4": 0
  },
  {
    "room": 2,
    "p1": { "0,2":  -1, "2,0":  -1, "1,2":  2},
    "p2": -1,
    "p3": 2,
    "p4": 1
  }
]
'''