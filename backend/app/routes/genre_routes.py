from flask import Blueprint, request, jsonify
from app.services.recommendation_service import RecommendationService

bp = Blueprint('genre', __name__, url_prefix='/recommend/genre')
recommendation_service = RecommendationService()

@bp.route('', methods=['POST'])
def recommend_by_genre():
    data = request.get_json()
    genres = data.get("genres", [])
    try:
        results = recommendation_service.recommend_by_genre(genres)
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}) 