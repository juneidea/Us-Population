from dash import Dash
from src.data.loader import load_population_data
from src.layout import create_layout

DATA_PATH = "./data/us-population-2010-2019-reshaped.csv"

def main() -> None:
    data = load_population_data(DATA_PATH)
    app = Dash()
    app.title = "US Population Dashboard"
    app.layout = create_layout(app, data)
    app.run()

if __name__ == "__main__":
    main()