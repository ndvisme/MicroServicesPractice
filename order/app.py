from flask import Flask
from routes import order_blueprint
from models import db, init_app
from flask_migrate import Migrate
import os
file_path = os.path.abspath(os.getcwd())+"./database/order.db"

app = Flask(__name__)

app.config['SECRET_KEY'] = 'vZK7siKrV8BL46KsyAIPoQ'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ file_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(order_blueprint)
init_app(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True, port=5003)