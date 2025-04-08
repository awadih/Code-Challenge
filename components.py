from utils.methods import *
import dash_bootstrap_components as dbc


def get_tabs(cities):
    tabs = []
    for city in cities:
        tabs.append(dbc.Card(
            dbc.CardBody(
                [
                    html.Div(
                        [
                            dbc.Col(
                                [
                                    dbc.Row(html.Div([
                                        generate_graphs(city=cities[city])])),
                                    dbc.Row(html.Div([
                                        html.Div([
                                            dbc.Button(
                                                "Speichern", id="Speichern-{}".format(cities[city]),
                                                className="me-2", n_clicks=0
                                            ),
                                            html.Span(id="span-speichern-{}".format(cities[city]),
                                                      style={"verticalAlign": "left"}),
                                            dcc.Download(id="Speichern-Data-{}".format(cities[city])),
                                        ]),
                                    ]))
                                ]
                            ),
                        ]
                    )
                ]
            ),
            className="mt-3",
        ))

    return dbc.Tabs(
        [
            dbc.Tab(tabs[0], label=list(cities.keys())[0]),
            dbc.Tab(tabs[1], label=list(cities.keys())[1]),
            dbc.Tab(tabs[2], label=list(cities.keys())[2]),
        ]
    )
