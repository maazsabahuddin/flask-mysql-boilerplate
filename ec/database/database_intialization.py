from flask_sqlalchemy import SQLAlchemy


def get_db(app):
    """
    App param for initializing database
    :param app:
    :return:
    """
    return SQLAlchemy(app)
