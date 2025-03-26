import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import os
import pickle
import requests
import zipfile
import io

class MovieRecommender:
    def __init__(self):
        self.current_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.movies = None
        self.ratings = None
        self.genre_columns = None
        self.item_similarity = None
        self.genre_similarity = None
        
    def download_dataset(self):
        """ML-100K 데이터셋을 다운로드합니다."""
        print("ML-100K 데이터셋을 다운로드합니다...")
        
        # 데이터 디렉토리 생성
        data_dir = os.path.join(self.current_dir, "data")
        ml_100k_dir = os.path.join(data_dir, "ml-100k")
        os.makedirs(ml_100k_dir, exist_ok=True)
        
        # ML-100K 데이터셋 다운로드 URL
        url = "https://files.grouplens.org/datasets/movielens/ml-100k.zip"
        
        try:
            # 데이터셋 다운로드
            response = requests.get(url)
            response.raise_for_status()
            
            # ZIP 파일 압축 해제
            with zipfile.ZipFile(io.BytesIO(response.content)) as zip_ref:
                # 필요한 파일만 추출
                for file in ['u.data', 'u.item']:
                    zip_ref.extract(file, ml_100k_dir)
                    
            print("데이터셋 다운로드가 완료되었습니다.")
            
        except Exception as e:
            print(f"데이터셋 다운로드 중 오류가 발생했습니다: {str(e)}")
            raise
        
    def load_data(self):
        """데이터를 로드합니다."""
        # ML-100K 데이터셋 경로
        data_dir = os.path.join(self.current_dir, "data/ml-100k")
        
        # 데이터셋이 없으면 다운로드
        if not os.path.exists(os.path.join(data_dir, 'u.data')) or \
           not os.path.exists(os.path.join(data_dir, 'u.item')):
            self.download_dataset()
        
        # 사용자-아이템 평점 데이터
        self.ratings = pd.read_csv(
            os.path.join(data_dir, 'u.data'),
            sep='\t',
            names=['userId', 'movieId', 'rating', 'timestamp']
        )
        
        # 영화 정보 데이터
        self.movies = pd.read_csv(
            os.path.join(data_dir, 'u.item'),
            sep='|',
            encoding='latin-1',
            names=['movieId', 'title', 'release_date', 'video_release_date',
                  'imdb_url', 'unknown', 'Action', 'Adventure', 'Animation',
                  'Children', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy',
                  'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi',
                  'Thriller', 'War', 'Western']
        )
        
        # 장르 컬럼 설정
        self.genre_columns = ['Action', 'Adventure', 'Animation', 'Children', 'Comedy',
                            'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir',
                            'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi',
                            'Thriller', 'War', 'Western']
        
        # 영화 정보 저장
        self.movies.to_csv(os.path.join(self.current_dir, "data/movies.csv"), index=False)
        
    def train(self):
        """모델을 학습합니다."""
        if self.movies is None or self.ratings is None:
            self.load_data()
            
        # 사용자-아이템 매트릭스 생성
        user_movie_matrix = self.ratings.pivot(
            index='movieId', 
            columns='userId', 
            values='rating'
        ).fillna(0)
        
        # 아이템 유사도 계산
        self.item_similarity = cosine_similarity(user_movie_matrix)
        
        # 장르 유사도 계산
        genre_matrix = self.movies[self.genre_columns].values
        self.genre_similarity = cosine_similarity(genre_matrix)
        
    def save_model(self):
        """학습된 모델을 저장합니다."""
        if self.item_similarity is None or self.genre_similarity is None:
            raise ValueError("모델이 학습되지 않았습니다.")
            
        # 모델 저장
        with open(os.path.join(self.current_dir, "data/item_similarity.pkl"), "wb") as f:
            pickle.dump(self.item_similarity, f)
            
        with open(os.path.join(self.current_dir, "data/genre_similarity.pkl"), "wb") as f:
            pickle.dump(self.genre_similarity, f)
            
        with open(os.path.join(self.current_dir, "data/genre_columns.pkl"), "wb") as f:
            pickle.dump(self.genre_columns, f)
            
    def load_model(self):
        """저장된 모델을 로드합니다."""
        with open(os.path.join(self.current_dir, "data/item_similarity.pkl"), "rb") as f:
            self.item_similarity = pickle.load(f)
            
        with open(os.path.join(self.current_dir, "data/genre_similarity.pkl"), "rb") as f:
            self.genre_similarity = pickle.load(f)
            
        with open(os.path.join(self.current_dir, "data/genre_columns.pkl"), "rb") as f:
            self.genre_columns = pickle.load(f)
            
        self.movies = pd.read_csv(os.path.join(self.current_dir, "data/movies.csv")) 