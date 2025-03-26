from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    # 블루프린트 등록
    from app.routes import movie_routes, genre_routes, mood_routes
    app.register_blueprint(movie_routes.bp)
    app.register_blueprint(genre_routes.bp)
    app.register_blueprint(mood_routes.bp)
    
    return app 