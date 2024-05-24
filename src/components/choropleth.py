from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
from src import ids

def render(app: Dash, df: pd.DataFrame, input_id, input_column) -> html.Div:
    @app.callback(
        Output(ids.US_MAP, "children"),
        [Input(ids.COLOR_DROPDOWN, "value"), Input(ids.YEAR_DROPDOWN, "value")]
    )
    def update_map(selected_color: str, selected_year: int) -> html.Div:
        choropleth = px.choropleth(df, locations=input_id, color=input_column, 
                                locationmode="USA-states",
                                color_continuous_scale=selected_color,
                                range_color=(0, max(df.population)),
                                scope="usa",
                                    labels={'population': 'Population'},
                                )
        choropleth.update_layout(
            margin=dict(l=0, r=0, t=0, b=0),
            height=350,
            width=650,
            dragmode=False,
        )
        return html.Div(
            children=[html.H2('Total Population ' + str(selected_year)), dcc.Graph(figure=choropleth)], id='map')

    return html.Div(id=ids.US_MAP)