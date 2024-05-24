import pandas as pd

class DataSchema:
    STATE = "states"
    STATE_CODE = "states_code"
    ID = "id"
    YEAR = "year"
    POPULATION = "population"
    COLOR = 'color'

def load_population_data(path: str) -> pd.DataFrame:
    # load the data from a CSV file
    data = pd.read_csv(
        path,
        dtype={
            DataSchema.STATE: str,
            DataSchema.STATE_CODE: str,
            DataSchema.ID: int,
            DataSchema.YEAR: int,
            DataSchema.POPULATION: int,
        }
    )
    return data