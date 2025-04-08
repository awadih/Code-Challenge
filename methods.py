from sqlite3 import Error
from dash import html, dcc
from utils.API_request import Request
import dash_bootstrap_components as dbc
import plotly.express as px
import sqlite3


def retrieve_data(city):
    """ returns a data table given the city and the page loading time / date """
    r = Request(city=city, days=4)
    return r.forcast()


def generate_graphs(city):
    """ returns a data plot given the city and the page loading time / date """
    r = Request(city=city, days=4)
    df = r.forcast()
    fig1 = px.line(data_frame=df, x=df['Datum/Uhr'],
                   y=df['Windgeschwindigkeit (Km/h)'], title='Prognosedaten für die Windgeschwindigkeit in Km/h')
    fig2 = px.line(data_frame=df, x=df['Datum/Uhr'],
                   y=df['Temperatur (Celsius)'], title='Prognosedaten für die Temperatur in Celsius')
    fig3 = px.line(data_frame=df, x=df['Datum/Uhr'],
                   y=df['Cloud coverage (Percent)'], title='Prognosedaten für Cloud Coverage in Prozent')
    fig1.update_yaxes(
        ticksuffix=" Km/h", showgrid=True
    )
    fig2.update_yaxes(
        ticksuffix=" °C", showgrid=True
    )
    fig3.update_yaxes(
        ticksuffix=" %", showgrid=True
    )

    return html.Div([
        dbc.Col([
            dbc.Row(html.Div([
                dcc.Graph(
                    id='graph-{}-fig1'.format(city),
                    figure=fig1
                ), ])),
            dbc.Row(html.Div([
                dcc.Graph(
                    id='graph-{}-fig2'.format(city),
                    figure=fig2
                ), ])),
            dbc.Row(html.Div([
                dcc.Graph(
                    id='graph-{}-fig3'.format(city),
                    figure=fig3
                ), ]))]), ])


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
