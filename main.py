from flask import Flask

from api import event_api
from data import db_session


app = Flask(__name__)

app.config['SECRET_KEY'] = 'what_is_secret_key'


def main():
    db_session.global_init('db/data.db')

    app.register_blueprint(event_api.blueprint)

    app.run()


if __name__ == '__main__':
    main()
