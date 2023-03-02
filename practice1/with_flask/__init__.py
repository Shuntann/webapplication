from flask import Flask


app = Flask(__name__)

import with_flask.main

from with_flask import db
db.create_NewMenu()