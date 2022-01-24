# Local Imports
from ec.database.database_intialization import get_db
from ec.utility import constants
from ec.config import config

# Framework Imports
from flask import Flask

app = Flask(__name__)


app.config[constants.SQLALCHEMY_DATABASE_URI] = config.MYSQL_URI

# initialize_db(app)
db = get_db(app)

from ec.views.v1.user import userAuthViews
