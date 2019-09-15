from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(
    __name__,
    instance_relative_config=True,
    template_folder="templates"
    )
# secret environment variables
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

import models


@app.route('/')
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run()
