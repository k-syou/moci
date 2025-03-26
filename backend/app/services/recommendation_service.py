import numpy as np
from app.services.data_service import DataService

class RecommendationService:
    def __init__(self):
        self.data_service = DataService()
        self.movies = self.data_service.load_movies()
        self.item_similarity = self.data_service.load_item_similarity()
        self.genre_similarity = self.data_service.load_genre_similarity()
        self.genre_columns = self.data_service.load_genre_columns()
        
        # 기분과 장르 매핑 정의
        self.mood_genre_mapping = {
            'happy': ['Comedy', 'Musical', 'Animation'],
            'sad': ['Drama', 'Romance'],
            'excited': ['Action', 'Adventure', 'Sci-Fi'],
            'romantic': ['Romance', 'Drama'],
            'scary': ['Horror', 'Thriller'],
            'thoughtful': ['Documentary', 'Drama'],
            'nostalgic': ['Drama', 'Romance'],
            'energetic': ['Action', 'Adventure'],
            'peaceful': ['Documentary', 'Drama'],
            'funny': ['Comedy', 'Animation']
        }
        
    def add_randomness(self, scores, randomness_factor=0.3):
        """유사도 점수에 랜덤 요소를 추가합니다."""
        max_score = np.max(scores)
        random_noise = np.random.uniform(0, max_score * randomness_factor, size=len(scores))
        return scores + random_noise
        
    def recommend_by_movie(self, title):
        idx = self.movies[self.movies["title"].str.lower() == title.lower()].index[0]
        similar_scores = self.item_similarity[idx]
        similar_scores = self.add_randomness(similar_scores)
        
        similar_indices = similar_scores.argsort()[-6:-1][::-1]
        return self.movies.iloc[similar_indices][["title", "release_date"]].to_dict(orient="records")
        
    def recommend_by_genre(self, genres):
        if not genres:
            raise ValueError("장르를 선택해주세요.")
            
        # 선택된 장르에 대한 가중치 계산
        genre_weights = np.zeros(len(self.genre_columns))
        for genre in genres:
            if genre in self.genre_columns:
                genre_weights[self.genre_columns.index(genre)] = 1

        # 장르 유사도 계산
        genre_scores = np.zeros(len(self.movies))
        for i in range(len(self.movies)):
            movie_genres = self.movies.iloc[i][self.genre_columns].values
            genre_scores[i] = np.sum(movie_genres * genre_weights)
        
        # 랜덤 요소 추가
        genre_scores = self.add_randomness(genre_scores)

        # 상위 5개 영화 추천
        similar_indices = genre_scores.argsort()[-6:-1][::-1]
        return self.movies.iloc[similar_indices][["title", "release_date"]].to_dict(orient="records")
        
    def recommend_by_mood(self, mood):
        if not mood:
            raise ValueError("기분을 입력해주세요.")
            
        mood = mood.lower()
        if mood not in self.mood_genre_mapping:
            raise ValueError("지원하지 않는 기분입니다. happy, sad, excited, romantic, scary, thoughtful, nostalgic, energetic, peaceful, funny 중 하나를 입력해주세요.")
            
        # 기분에 맞는 장르 선택
        recommended_genres = self.mood_genre_mapping[mood]
        
        # 선택된 장르에 대한 가중치 계산
        genre_weights = np.zeros(len(self.genre_columns))
        for genre in recommended_genres:
            if genre in self.genre_columns:
                genre_weights[self.genre_columns.index(genre)] = 1

        # 장르 유사도 계산
        genre_scores = np.zeros(len(self.movies))
        for i in range(len(self.movies)):
            movie_genres = self.movies.iloc[i][self.genre_columns].values
            genre_scores[i] = np.sum(movie_genres * genre_weights)
        
        # 랜덤 요소 추가
        genre_scores = self.add_randomness(genre_scores)

        # 상위 5개 영화 추천
        similar_indices = genre_scores.argsort()[-6:-1][::-1]
        return self.movies.iloc[similar_indices][["title", "release_date"]].to_dict(orient="records") 