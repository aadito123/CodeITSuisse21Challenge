import logging
import json
import collections
import requests
from functools import lru_cache
from flask import request, jsonify

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
        self.gridMapNum = [[0]*(self.maxX+1) for i in range(self.maxY+1)]

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

    def minPathSum(self):
        row = self.maxY
        column = self.maxX
        i=row-1
        j=column-1
        while j>=0:
            self.gridMapNum[row][j]+=self.gridMapNum[row][j+1]
            j-=1
        while i>=0:
            self.gridMapNum[i][column]+=self.gridMapNum[i+1][column]
            i-=1
        j=column-1
        i = row-1
        while i>=0:
            while j>=0:
                self.gridMapNum[i][j] += min(self.gridMapNum[i][j+1],self.gridMapNum[i+1][j])
                j-=1
            j=column-1
            i-=1
        return(self.gridMapNum[0][0])

            
    def solve(self):
        symbol = ['', 'S', 'M', 'L']
        for y in range(self.maxY+1):
            for x in range(self.maxX+1):
                self.gridMapNum[y][x] = 3 - (self.value(x, y)%3)
                self.gridMap[y][x] = symbol[self.gridMapNum[y][x]]
        return {"gridMap": self.gridMap, "minimumCost": self.minPathSum()-3}

@app.route('/stock-hunter', methods=['POST'])
def evaluateStockHunter():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    result = []
    for maze in data:
        result.append(Solve(maze).solve())
    logging.info("My result :{}".format(result))
    return json.dumps(result)
