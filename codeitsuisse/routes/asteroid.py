import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

def multiplierScore(streak):
    if streak >= 10:
        return 2*streak
    if streak >= 7:
        return 1.5*streak
    else:
        return streak

def testDetonate(index, asteroid, asteroidCount):
    total = 1
    score = 1
    left = index - 1
    right = index + 1
    streak = 0
    currentType = asteroid[left]
    leftType = asteroid[left]
    rightType = asteroid[right]
    while left >= 0 and right <= asteroidCount - 1:
        while leftType == currentType and left > 0:
            streak += 1
            left -= 1
            leftType = asteroid[left]
        while rightType == currentType and right < asteroidCount - 1:
            streak += 1
            right += 1
            rightType = asteroid[right]
        
        streak += (rightType == currentType) + (leftType == currentType)
        total += streak
        #logging.info("{}: {}".format(currentType, multiplierScore(streak)))
        score += multiplierScore(streak)
        if right == asteroidCount - 1 and left == 0:    
            break

        streak = 0
        if leftType == rightType:
            currentType = leftType
        else:
            break   
    return (index, score, total)  

def solve(asteroids):
    scores = []
    asteroidCount = len(asteroids)
    previous = ''
    flag = True
    for index, char in enumerate(asteroids[1:], 1):
        if char == previous:
            continue
        else:
            if index == asteroidCount - 1:
                break
            sameAsBefore = asteroids[index - 1] == char
            sameAsAfter = asteroids[index + 1] == char
            if asteroids[index - 1] == asteroids[index + 1]:
                #logging.info("{}, {}, {}".format(char, asteroids[index - 1], asteroids[index + 1]))
                scores.append(testDetonate(index, asteroids, asteroidCount))
                #logging.info("-------------------")
                previous = char
            elif not sameAsAfter:
                previous = char

    # logging.info("Scores: {}".format(scores))
    return max(scores, default= (0,0,0),key=lambda x: x[2])

@app.route('/asteroid', methods=['POST'])
def evaluateAsteroid():
    asteroidsList = request.get_json().get('test_cases')
    logging.info("data sent for evaluation {}".format(asteroidsList))
    result = []
    for asteroids in asteroidsList:
        solution = solve(asteroids)
        #logging.info("############")
        result.append({"input": asteroids, "score": solution[1], "origin": solution[0]})

    logging.info("My result :{}".format(result))
    return json.dumps(result)
