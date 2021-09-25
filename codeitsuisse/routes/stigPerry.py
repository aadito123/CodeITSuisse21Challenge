import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

class Solve:
    def __init__(self, interview):
        self.questions = interview['questions']
        self.max = interview['maxRating']        

    def solve(self):
        maxiFrom = min(self.questions, key=lambda interval: interval[0]['from'])
        miniTo = max(self.questions, key=lambda interval: interval[0]['to'])
        logging.info("Max: {}, Min: {}".format(maxiFrom, miniTo))
        return {}

@app.route('/stig/perry', methods=['POST'])
def evaluateOptopt():
    interviews = request.get_json()
    #logging.info("data sent for evaluation {}".format(data))
    result = []
    for interview in interviews:
        result.append(Solve(interview).solve())
    logging.info("My result :{}".format(result))
    return json.dumps(result)

'''

 Proposed solution:[Result(p=175811, q=1000000000), 
 Result(p=87803, q=500000000), 
 Result(p=35151, q=200000000), 
 Result(p=35127, q=200000000), 
 Result(p=43931, q=250000000)] / 
 Candidate's solution: [Result(p=0, q=0), Result(p=0, q=0), Result(p=0, q=0), Result(p=0, q=0), Result(p=0, q=0)]
'''