import pandas as pd
import pickle
import os

class DataService:
    def __init__(self):
        self.current_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        
    def load_movies(self):
        return pd.read_csv(os.path.join(self.current_dir, "data/movies.csv"))
        
    def load_item_similarity(self):
        with open(os.path.join(self.current_dir, "data/item_similarity.pkl"), "rb") as f:
            return pickle.load(f)
            
    def load_genre_similarity(self):
        with open(os.path.join(self.current_dir, "data/genre_similarity.pkl"), "rb") as f:
            return pickle.load(f)
            
    def load_genre_columns(self):
        with open(os.path.join(self.current_dir, "data/genre_columns.pkl"), "rb") as f:
            return pickle.load(f) 