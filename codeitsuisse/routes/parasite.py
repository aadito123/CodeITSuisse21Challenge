import logging
import json 

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

class Solver:
    def __init__(self, room):
        self.grid = room['grid']
        self.room = room['room']
        self.stringInd = room['interestedIndividuals']
        self.intInd = [(int(tup.split(',')[0]), int(tup.split(',')[1])) for tup in room['interestedIndividuals']]
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
        self.cache = [[-1]*self.col for i in range(self.row)]

    def pathFind(self, intInd):
        grid = [row[:] for row in self.grid]
        
        length = 0
        # directions
        Dir = ((0, 1), (0, -1), (1, 0), (-1, 0))
        # queue
        q = []
        # insert the top right corner.
        q.append(intInd)
        # until queue is empty
        while(len(q) > 0) :
            p = q[0]
            q.pop(0)
            # mark as visited
            grid[p[0]][p[1]] = -1
            # destination is reached.
            if(self.cache[p[0]][p[1]] != -1):
                self.cache[intInd[0]][intInd[1]] = length + self.cache[p[0]][p[1]]
                return length + self.cache[p[0]][p[1]]
            if(p == self.infected) :
                self.cache[intInd[0]][intInd[1]] = length
                return length
            # check all four directions
            move = False
            for i in Dir :
                # using the direction array
                a = p[0] + i[0]
                b = p[1] + i[1]
                # not blocked and valid
                if(a >= 0 and b >= 0 and a < self.row and b < self.col and (grid[a][b] == 1 or grid[a][b] == 3)):
                    q.append((a, b))
                    length += 1
                    move = True
            if not move:
                length -= 1
        return -1

    def solveP1(self, intInd):
        if self.grid[intInd[0]][intInd[1]] == 0 or self.grid[intInd[0]][intInd[1]] == 2:
            return -1
        else:
            return self.pathFind(intInd)
        pass

    def p1(self, stringInd):
        p1Dict = {}
        for i, intIn in enumerate(self.intInd):
            p1Dict[stringInd[i]] = self.solveP1(intIn)
        logging.info("P1: {}".format(p1Dict))
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
        retDict['p1'] = self.p1(self.stringInd)
        retDict['p2'] = self.p2()
        retDict['p3'] = self.p3()
        retDict['p4'] = self.p4()
        return retDict

    

@app.route('/parasite', methods=['POST'])
def evaluateParasite():
    logging.info("endpoint called")
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