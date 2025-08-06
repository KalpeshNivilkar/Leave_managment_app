from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import Config
from models import db
from routes.auth_routes import auth_bp
from routes.user_routes import user_bp
from routes.leave_routes import leave_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
jwt = JWTManager(app)

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(user_bp, url_prefix="/users")
app.register_blueprint(leave_bp, url_prefix="/leave")

@app.route('/')
def index():
    return "Leave Management System API is running!", 200
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
