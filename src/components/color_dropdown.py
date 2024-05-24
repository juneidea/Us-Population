from dash import html, dcc
from src import ids

def render() -> html.Div:
    color_theme_list = ['turbo', 'blues', 'greens', 'reds', 'cividis', 'magma', 'plasma', 'rainbow', 'viridis']

    return html.Div(
        children=[
            html.Div('Select a color theme', style={'color': '#999'}),
            dcc.Dropdown(
                id=ids.COLOR_DROPDOWN,
                options=[{"label": color, "value": color} for color in color_theme_list],
                value=color_theme_list[0],
                clearable=False,
            )
        ]
    )