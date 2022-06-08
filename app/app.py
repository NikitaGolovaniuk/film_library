from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes import home


app = Flask(__name__)

db = SQLAlchemy(app)

app.add_url_rule('/', view_func=home.index)

if __name__ == '__main__':
    app.run(debug=True)




