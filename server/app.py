from models import db, Sweet, Vendor, VendorSweet
from flask_migrate import Migrate
from flask import Flask, render_template
from flask_restful import Api, Resource
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = f"postgresql://austine:bgzkz8jvlCZUQkI1A8Q45JEYmewMqviS@dpg-coigeldjm4es739nlpng-a.oregon-postgres.render.com/austinemain"
#DATABASE= os.environ.get('DATABASE_URI')
app = Flask(__name__,
    static_url_path='',
    static_folder='../client/build',
    template_folder='../client/build')
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

from routes import *

@app.errorhandler(404)
def not_found(e):
    return render_template("index.html"), 404


if __name__ == '__main__':
    app.run(debug=True)
