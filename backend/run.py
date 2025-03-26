from app import create_app
from train import main
import os
app = create_app()

if __name__ == "__main__":
    try:
        if not os.path.exists("data/movies.csv"):
            main()
    except Exception as e:
        print(f"Error: {e}")
        exit()
    app.run(debug=True)