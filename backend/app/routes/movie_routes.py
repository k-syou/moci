from flask import Blueprint, request, jsonify
from app.services.recommendation_service import RecommendationService

bp = Blueprint('movie', __name__, url_prefix='/recommend/movie')
recommendation_service = RecommendationService()

@bp.route('', methods=['POST'])
def recommend_by_movie():
    data = request.get_json()
    title = data.get("title")
    try:
        results = recommendation_service.recommend_by_movie(title)
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}) 