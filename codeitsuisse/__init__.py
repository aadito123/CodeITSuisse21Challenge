from flask import Flask
app = Flask(__name__)

import codeitsuisse.routes.secret_message
import codeitsuisse.routes.square
import codeitsuisse.routes.tictactoe
import codeitsuisse.routes.parasite
import codeitsuisse.routes.asteroid
import codeitsuisse.routes.stigPerry
import codeitsuisse.routes.fixedrace
import codeitsuisse.routes.stock_hunter