from dash import dcc, html
import dash_vega_components as dvc
import pandas as pd
import altair as alt
import plotly.graph_objects as go

def format_number(num):
    if num > 1000000:
        if not num % 1000000:
            return f'{num // 1000000}M'
        return f'{round(num / 1000000, 1)}M'
    return f'{num // 1000}K'

def round_percent(num1, num2):
    return str(round((num1/num2)*100, 1)) + '%'

def make_donut(percent, input_text, input_color):
    if input_color == 'green':
        chart_color = ['#59ad7c', '#12783D']
    if input_color == 'red':
        chart_color = ['#E74C3C', '#781F16']

    source = pd.DataFrame({
        "Topic": ['', input_text],
        "% value": [10-percent, percent]
    })
    source_bg = pd.DataFrame({
        "Topic": ['', input_text],
        "% value": [10, 0]
    })

    plot = alt.Chart(source).mark_arc(innerRadius=45, cornerRadius=25).encode(
        theta="% value",
        color= alt.Color("Topic:N",
                      scale=alt.Scale(
                          #domain=['A', 'B'],
                          domain=[input_text, ''],
                          # range=['#29b5e8', '#155F7A']),  # 31333F
                          range=chart_color),
                      legend=None),
    ).properties(width=130, height=130)
    text = plot.mark_text(align='center', color="#59ad7c", font="Lato", fontSize=28, fontWeight=700, fontStyle="italic").encode(text=alt.value(f'{str(percent)} %'))
    plot_bg = alt.Chart(source_bg).mark_arc(innerRadius=45, cornerRadius=20).encode(
        theta="% value",
        color= alt.Color("Topic:N",
                      scale=alt.Scale(
                          # domain=['A', 'B'],
                          domain=[input_text, ''],
                          range=chart_color),  # 31333F
                      legend=None),
        ).properties(width=130, height=130)
    return plot_bg + plot + text

def render(df: pd.DataFrame, i: int) -> html.Div:
    name = df.states.iloc[i]
    population = format_number(df.population.iloc[i])
    delta = 'Decrease' if df.population_difference.iloc[i] < 0 else 'Increase'

    fig = go.Figure(
        go.Indicator(
        mode = "delta",
        value = round(df.population_difference.iloc[i], -3),
        delta = {'reference': 0},
    ))
    fig.update_layout(
    margin=dict(l=0, r=25, t=0, b=0),
)

    percent_diff = round((df.population_difference.iloc[i]/df.population.iloc[i])*100, 1)
    donut = make_donut(percent_diff * -1, 'Outbound Migration', 'red') if percent_diff < 0 else make_donut(percent_diff, 'Inbound Migration', 'green')
    return html.Div(
                children=[
                    html.Div(
                        children=[                    
                            html.Div(name, style={'font-size': '1rem', 'margin': '5px', 'font-weight': '600', 'min-width': '110px'}),
                            html.Div('Population', style={'font-size': '0.5rem', 'margin': '5px 0 0 5px', 'font-weight': '300', 'color': '#aaa'}),
                            html.Div(population, style={'font-size': '1.25rem', 'margin': '0 0 5px 5px', 'font-weight': '600'}),
                            html.Div(delta, style={'font-size': '0.5rem', 'margin': '5px 0 0 5px', 'font-weight': '300', 'color': '#aaa'}),
                            dcc.Graph(figure=fig, style={"height": 30, "width": 100}),
                        ]
                    ),
                    dvc.Vega(
                        id="altair-chart",
                        opt={"renderer": "svg", "actions": False},
                        spec=donut.to_dict(),
                    ),
                ],
                id='card',
                style={
                    'display': 'flex',
                    'border-radius': '9px',
                    'margin': '5px',
                    'padding': '15px',
                }
            )


    