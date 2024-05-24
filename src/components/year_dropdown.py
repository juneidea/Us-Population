from dash import html, dcc
import pandas as pd
from ..data.loader import DataSchema
from src import ids

def render(data: pd.DataFrame) -> html.Div:
    all_years: list[int] = data[DataSchema.YEAR].tolist()
    unique_years = sorted(set(all_years), key=int, reverse=True)

    return html.Div(
        children=[
            html.Div('Select a year', style={'color': '#999'}),
            dcc.Dropdown(
                id=ids.YEAR_DROPDOWN,
                options=[{"label": year, "value": year} for year in unique_years],
                value=unique_years[0],
                clearable=False,
            )
        ]
    )