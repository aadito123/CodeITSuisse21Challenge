import logging
import json 
import collections
from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

class Solver:
    def __init__(self, room):
        self.grid = room['grid']
        self.room = room['room']
        self.intInd = [((int(tup.split(',')[0]), int(tup.split(',')[1])), tup) for tup in room['interestedIndividuals']]
        #logging.info("Room: {}".format(self.intInd))
        self.infected = (-1, -1)
        self.row = len(self.grid)
        self.col = len(self.grid[0])
        for i in range(self.row):
            for j in range(self.col):
                if self.grid[i][j] == 3:
                    self.infected = (i, j)
                    break
            if self.infected != (-1, -1):
                break
        self.cache = {}

    def pathFind(self, intInd):
        queue = collections.deque([[intInd]])
        seen = set([intInd])
        while queue:
            path = queue.popleft()
            x, y = path[-1]
            if (x, y) in self.cache.keys():
                return len(path) + self.cache[(x, y)]
            if (x, y) == self.infected:
                self.cache[intInd] = len(path) - 1
                return self.cache[intInd]
            for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
                if 0 <= x2 < self.col and 0 <= y2 < self.row and self.grid[y2][x2] != 0 and self.grid[y2][x2] != 2 and (x2, y2) not in seen:
                    queue.append(path + [(x2, y2)])
                    seen.add((x2, y2))
        return -1

    def solveP1(self, intInd):
        if self.grid[intInd[0]][intInd[1]] == 0 or self.grid[intInd[0]][intInd[1]] == 2:
            return -1
        else:
            return self.pathFind(intInd)
        pass

    def p1(self):
        p1Dict = {}
        for intIn in self.intInd:
            p1Dict[intIn[1]] = self.solveP1(intIn[0])
        #logging.info("P1: {}".format(p1Dict))
        return p1Dict

    def p2(self):
        return 1

    def p3(self):
        return 1

    def p4(self):
        return 1

    def solve(self):
        retDict = {}
        retDict['room'] = self.room
        retDict['p1'] = self.p1()
        retDict['p2'] = self.p2()
        retDict['p3'] = self.p3()
        retDict['p4'] = self.p4()
        return retDict

    

@app.route('/parasite', methods=['POST'])
def evaluateParasite():
    #logging.info("endpoint called")
    rooms = request.get_json()
    logging.info("data sent for evaluation {}".format(rooms))
    result = []
    for room in rooms:
        result.append(Solver(room).solve())

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