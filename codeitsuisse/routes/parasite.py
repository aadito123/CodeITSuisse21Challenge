import logging
import json 

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

def pathFind(arr, intInd, infected, border):
    grid = [row[:] for row in arr]
    row, col = border
    length = 0
    # directions
    Dir = [ [0, 1], [0, -1], [1, 0], [-1, 0]]
    # queue
    q = []
    # insert the top right corner.
    q.append(infected)
    # until queue is empty
    while(len(q) > 0) :
        p = q[0]
        q.pop(0)
        # mark as visited
        grid[p[0]][p[1]] = -1
        # destination is reached.
        if(p == intInd) :
            return length
        # check all four directions
        move = False
        for i in range(4) :
            # using the direction array
            a = p[0] + Dir[i][0]
            b = p[1] + Dir[i][1]
            # not blocked and valid
            if(a >= 0 and b >= 0 and a < row and b < col and grid[a][b] == 1):
                print((a, b))           
                q.append((a, b))
                length += 1
                move = True
        if not move:
            length -= 1
    return -1

def solveP1(intInd, grid, infected, border):
    if grid[intInd[0]][intInd[1]] == 0 or grid[intInd[0]][intInd[1]] == 2:
        return -1
    else:
        return pathFind(grid, intInd, infected, border)
    pass

def p1(grid, intInd, stringInd, infected, border):
    p1Dict = {}
    for i, intIn in enumerate(intInd):
        p1Dict[stringInd[i]] = solveP1(intIn, grid, infected, border)
    logging.info("P1: {}".format(p1Dict))
    pass

def p2(grid, infected, border):
    return 1

def p3(grid, infected, border):
    return 1

def p4(grid, infected, border):
    return 1

def solveForRoom(room):
    grid = room['grid']
    intInd = [(int(tup.split(',')[0]), int(tup.split(',')[1])) for tup in room['interestedIndividuals']]
    logging.info("Room: {}".format(intInd))
    infected = (-1, -1)
    row = len(grid)
    col = len(grid[0])
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 3:
                infected = (i, j)
                break
        if infected != (-1, -1):
            break
    retDict = {}
    retDict['room'] = room['room']
    retDict['p1'] = p1(grid, intInd, room['interestedIndividuals'], infected, (row, col))
    retDict['p2'] = p2(grid, infected, (row, col))
    retDict['p3'] = p3(grid, infected, (row, col))
    retDict['p4'] = p4(grid, infected, (row, col))

@app.route('/parasite', methods=['GET'])
def evaluateParasite():
    logging.info("endpoint called")
    rooms = request.get_json()
    logging.info("data sent for evaluation {}".format(rooms))
    result = []
    for room in rooms:
        result.append(solveForRoom(room))

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