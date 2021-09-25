import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)


@app.route('/encryption', methods=['POST'])
def evaluateSecretMessage():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    # inputValue = data.get("input");
    result = []
    for test_case in data:
        result.append(encrypt(test_case["n"], test_case["text"]))

    logging.info("My result :{}".format(result))
    return jsonify(result)


def encrypt(n, text):
    # removing spaces and non alpha num characters
    processed_text = ""
    for ch in text:
        if ch.isalnum():
            processed_text += ch.upper()

    # encrypt the string
    string_length = len(processed_text)
    result = ['']*string_length
    for i in range(string_length):
        result[i] = processed_text[(3*i) % string_length]
    return ''.join(result)

#                   0:7    7:14    14:20
# 20 characters, 7 char, 7 char, 6 char
# Thisisa
# samplem
# essage

# n = 3
# TSEHASIMSSPAILGSEEAM
