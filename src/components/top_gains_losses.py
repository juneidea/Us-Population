from dash import Dash, html
from dash.dependencies import Input, Output
import pandas as pd
from src import ids
from src.components import card

def calculate_population_difference(df: pd.DataFrame, selected_year):
    current_year_data = df[df['year'] == selected_year].reset_index()
    previous_year_data = df[df['year'] == selected_year - 1].reset_index()
    current_year_data['population_difference'] = current_year_data.population.sub(previous_year_data.population, fill_value=0)
    return pd.concat([current_year_data.states, current_year_data.id, current_year_data.population, current_year_data.population_difference], axis=1).sort_values(by="population_difference", ascending=False)

def render(app: Dash, df: pd.DataFrame) -> html.Div:
    @app.callback(
        Output(ids.TOP_GAINS, "children"),
        Input(ids.YEAR_DROPDOWN, "value")
    )
    def update_top_gains(selected_year: int) -> html.Div:
        df_population_difference_sorted = calculate_population_difference(df, selected_year)
        return html.Div(
            children=[
                html.Div(
                    children=[
                        html.H2('Top Gains'),
                        html.Div(
                            children=[
                                card.render(df_population_difference_sorted, 0),
                                card.render(df_population_difference_sorted, 1),
                                card.render(df_population_difference_sorted, 2),
                            ],
                            id='gains',
                            style={'display': 'flex'},
                        ),
                    ]
                ),
                html.Div(
                    children=[
                        html.H2('Top Losses'),
                        html.Div(
                            children=[
                            card.render(df_population_difference_sorted, -1),
                            card.render(df_population_difference_sorted, -2),
                            card.render(df_population_difference_sorted, -3),
                            ],
                            id='losses',
                            style={'display': 'flex'},
                        ),
                    ],
                )
            ]
        )
    
    return html.Div(id=ids.TOP_GAINS)