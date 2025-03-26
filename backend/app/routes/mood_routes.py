from flask import Blueprint, request, jsonify
from app.services.recommendation_service import RecommendationService

bp = Blueprint('mood', __name__, url_prefix='/recommend/mood')
recommendation_service = RecommendationService()

@bp.route('', methods=['POST'])
def recommend_by_mood():
    data = request.get_json()
    mood = data.get("mood", "")
    try:
        results = recommendation_service.recommend_by_mood(mood)
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}) 