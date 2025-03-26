from app.models.model import MovieRecommender

def main():
    # 모델 초기화 및 학습
    recommender = MovieRecommender()
    recommender.load_data()
    recommender.train()
    
    # 모델 저장
    recommender.save_model()
    print("모델 학습 및 저장이 완료되었습니다.")

if __name__ == "__main__":
    main() 