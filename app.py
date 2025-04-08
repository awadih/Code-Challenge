from dash import ctx, Output, Input
from datetime import datetime
from components.components import get_tabs
from utils.methods import *
import dash_bootstrap_components as dbc
import sqlite3
import dash

# Today
today = datetime.today()

# Dash App with external bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Prognose Challenge Impuls"

# Get Tabs for layout
cities = {'Köln': 'Cologne', 'Berlin': 'Berlin', 'München': 'Munich'}
tabs = get_tabs(cities=cities)

# Define the app-layout
app.layout = html.Div([
    html.Div([dbc.Container(
        [
            html.H1("Code Challenge Impuls", className="display-3"),
            html.P(
                "Prognosedaten über API für Windgeschwindigkeit, Temperatur und Cloud Coverage - "
                "Orte: Köln, München und Berlin",
                className="lead",
            ),
            html.Hr(className="my-2"),
            html.P(
                "Heute ist der {}".format(datetime.today().strftime("%d.%m.%Y")),
            ),
        ],
        fluid=True,
        className="py-3",
    )]),
    html.Div([
        tabs,
        html.Div(id='tabs-content-example-graph')
    ])
])


@app.callback(
    Output("Speichern-Data-Cologne", "data"),
    Input("Speichern-Cologne", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    if "Speichern-Cologne" == ctx.triggered_id:
        df = retrieve_data('Cologne')
        create_connection('myDatabase.db')
        conn = sqlite3.connect('myDatabase.db')
        df.to_sql(name='Cologne', con=conn, if_exists='append')
    else:
        return None
    return dcc.send_data_frame(df.to_csv, "prognosedaten-Köln-{}.csv".format(datetime.now()))


@app.callback(
    Output("Speichern-Data-Munich", "data"),
    Input("Speichern-Munich", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    if "Speichern-Munich" == ctx.triggered_id:
        df = retrieve_data('Munich')
        create_connection('myDatabase.db')
        conn = sqlite3.connect('myDatabase.db')
        df.to_sql(name='Munich', con=conn, if_exists='append')
    else:
        return None
    return dcc.send_data_frame(df.to_csv, "prognosedaten-München-{}.csv".format(datetime.now()))


@app.callback(
    Output("Speichern-Data-Berlin", "data"),
    Input("Speichern-Berlin", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    if "Speichern-Berlin" == ctx.triggered_id:
        df = retrieve_data('Berlin')
        create_connection('myDatabase.db')
        conn = sqlite3.connect('myDatabase.db')
        df.to_sql(name='Berlin', con=conn, if_exists='append')
    else:
        return None
    return dcc.send_data_frame(df.to_csv, "prognosedaten-Berlin-{}.csv".format(datetime.now()))


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
