from flask import Flask

from data import db_session


app = Flask(__name__)
app.config['SECRET_KEY'] = 'what_is_secret_key'


def main():
    app.run()


if __name__ == '__main__':
    main()
