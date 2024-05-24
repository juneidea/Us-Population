from dash import Dash, dash_table, html
from dash.dependencies import Input, Output
import pandas as pd
from src import ids

def render(app: Dash, df: pd.DataFrame) -> html.Div:
    @app.callback(
        Output(ids.POPULATION_TABLE, "children"),
        Input(ids.YEAR_DROPDOWN, "value")
    )
    def update_population_table(selected_year: int) -> html.Div:
        df_selected_year = df[df.year == selected_year]
        df_sorted_pop = df_selected_year.sort_values(by="population", ascending=False)
        sum_population = df_sorted_pop['population'].sum()
        round_population = round(sum_population / 1000000, 1)
        million_string = str(round_population) + ' M'
        df_sorted_pop['percentage'] = round((df_sorted_pop['population'] / sum_population) * 100, 1)
        top_population = df_sorted_pop.population.iloc[0]
        df_sorted_pop['meter'] = '<meter id="disk_c" value="' + df_sorted_pop['population'].apply(str) + '" min="0" max="' + str(top_population) +'"></meter>'

        return html.Div(
            children=[
                html.H2(million_string),
                dash_table.DataTable(
                df_sorted_pop.to_dict('records'),
                columns=[{'name': 'State', 'id': 'states', 'type': 'text'}, 
                         {'name': 'Population', 'id': 'population', 'type': 'numeric'}, 
                         {'name': '', 'id': 'meter', 'presentation': 'markdown'},
                         {'name': '%', 'id': 'percentage', 'type': 'numeric'}],
                markdown_options={"html": True},
                )],
                id='population'
            )

    return html.Div(id=ids.POPULATION_TABLE)