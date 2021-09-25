import logging
import json
import requests
from functools import lru_cache
from flask import request, jsonify
from numpy import array
#from flask_sse import sse

from codeitsuisse import app

logger = logging.getLogger(__name__)

class Solve:
    def __init__(self, maze):    
        self.entryX = maze['entryPoint']['first']
        self.entryY = maze['targetPoint']['second']
        self.maxX = maze['targetPoint']['first']
        self.maxY = maze['targetPoint']['second']
        self.gridDepth = maze['gridDepth']
        self.gridKey = maze['gridKey']
        self.horStep = maze['horizontalStepper']
        self.verStep = maze['verticalStepper']
        self.gridMap = [[0]*(self.maxX+1) for i in range(self.maxY+1)]

    def riskLevel(self, integer, step):
        integer = integer*step + self.gridDepth
        return integer%self.gridKey

    @lru_cache(maxsize=None)
    def value(self, x, y):
        if (x, y) == (0, 0) or (x, y) == (self.maxX, self.maxY):
            return 0
        if not x:
            return self.riskLevel(y, self.verStep)
        if not y:
            return self.riskLevel(x, self.horStep)
        one = self.value(x - 1, y)
        two = self.value(x, y - 1)
        return self.riskLevel(one*two, 1)
        
    def solve(self):
        symbol = ['L', 'M', 'S']
        for y in range(self.maxY+1):
            for x in range(self.maxX+1):
                self.gridMap[y][x] = self.value(x, y)%3
        print(self.gridMap)


@app.route('/stock-hunter', methods=['POST'])
def evaluateStockHunter():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    result = []
    for maze in data:
        result.append(Solve(maze).solve())
    logging.info("My result :{}".format(result))
    return json.dumps(result)
