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
    score = 0
    left = index
    right = index
    total = 1
    streak = 1
    currentType = asteroid[index]
    leftType = currentType
    rightType = currentType
    while left > 0 and right < asteroidCount - 1:
        while leftType == currentType and left > 0:
            streak += 1
            total += 1
            left -= 1
            leftType = asteroid[left]
        while rightType == currentType and right < asteroidCount - 1:
            streak += 1
            total += 1
            right += 1
            rightType = asteroid[right]
        score += multiplierScore(streak)
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
            # logging.info("{}, {}, {}".format(char, asteroids[index - 1], asteroids[index + 1]))
            if asteroids[index - 1] == asteroids[index + 1]:
                scores.append(testDetonate(index, asteroids, asteroidCount))
                char = previous
            elif sameAsBefore:
                char = previous
            elif not sameAsAfter:
                char = previous
    # logging.info("Scores: {}".format(scores))
    return max(scores, default= (0,0),key=lambda x: x[2])

@app.route('/asteroid', methods=['POST'])
def evaluateAsteroid():
    asteroidsList = request.get_json().get('test_cases')
    logging.info("data sent for evaluation {}".format(asteroidsList))
    result = []
    for asteroids in asteroidsList:
        solution = solve(asteroids)
        result.append({"input": asteroids, "score": solution[1], "origin": solution[0]})

    logging.info("My result :{}".format(result))
    return json.dumps(result)
