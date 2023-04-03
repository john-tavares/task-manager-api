from flask import Flask
from flask_migrate import Migrate
from config import *
from api.views import api_bp
from database import db

app = Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)
migrate = Migrate(app, db)

# Register Blueprints
app.register_blueprint(api_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=DEBUG)