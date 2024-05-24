from dash import Dash, html
import pandas as pd
from src.data.loader import DataSchema
from src.components import top_gains_losses, year_dropdown, color_dropdown, pop_table, choropleth

def create_layout(app: Dash, df: pd.DataFrame) -> html.Div:
    return html.Div(
        className="app-container",
        children=[
            html.Div(
                className="app-div",
                children=[
                    html.H1(app.title),
                    html.Div(
                        children=[
                            year_dropdown.render(df),
                            color_dropdown.render(),
                        ],
                        style={'display': 'flex'}
                    ),
                    html.Div(
                        children=[
                            choropleth.render(app, df, DataSchema.STATE_CODE, DataSchema.POPULATION),
                            pop_table.render(app, df),
                        ],
                        style={'display': 'flex'}
                    ),
                    top_gains_losses.render(app, df)
                ]
            )
        ]
    )