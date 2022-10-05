import colorsys
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def main():
    print("hey there")
    # open csv to read
    # open another csv to write
    # iterate over each row, filter pink morsel and combine the quantity and price
    # write each row after combining the fields
    
    df = pd.read_csv("C:\\Users\\Akshay bruh\\Desktop\\quantium-starter\\data\\all_csv_files.csv")
    print(df)

    #remove duplicates
    if len(df[df.duplicated()]):
        df.drop_duplicates(keep='first',inplace=True)
    df = df[df['product'] == "pink morsel"]
    print("----filtered df------")
    print(df)

    df = df.replace("[$]", "", regex=True)

    print("----dollar removed df------")
    print(df)

    df["sales"] = df["price"].astype(float) * df["quantity"].astype(float)
    df2 = df.drop(["quantity", "price"], axis=1)
    print("----final df------")
    print(df2)

    df2.to_csv("C:\\Users\\Akshay bruh\\Desktop\\quantium-starter\\data\\final_csv.csv", encoding='utf-8', index=False)
# #creating a dash layout
    app = Dash(__name__)

    colors = {
    'background': 'pink',
    'text': '#7FDBFF'
    }

    # fig = px.line(df2, x="date", y="sales", color="region")

    app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
        html.H1(
            children='SoulFoods',
            style={
              'textAlign': 'center',
              'color': colors['text']
              },
        ),
        html.Div(children='''Pink morsel sales over time.''',  style={
            'textAlign': 'center',
            'color': colors['text']
        }),

        html.Div([
            html.Br(),
            html.Label(['Region:'], style={'font-weight': 'bold'}),
            dcc.RadioItems(
                id='xradioitem',
                options=[
                    {'label': 'All', 'value':'All'},
                    # {'label': 'north', 'value':'north'},
                    # {'label': 'south', 'value':'south'},
                    # {'label': 'east', 'value':'east'},
                    # {'label': 'west', 'value':'west'},

                ],
                value = 'All',
                style={"width":"50%"}

            ),
        ]),

        html.Div([
            html.Br(),
            html.Label(['Region:'], style={'font-weight': 'bold'}),
            dcc.RadioItems(
                id='yradioitem',
                options=[
                 
                    {'label': 'north', 'value':'north'},
                    {'label': 'south', 'value':'south'},
                    {'label': 'east', 'value':'east'},
                    {'label': 'west', 'value':'west'},

                ],
                # value = 'north',
                style={"width":"50%"}

            ),

        ]),

        dcc.Graph(
        id='example-graph',
        # figure=fig
        )
    ])

    @app.callback(
        Output(component_id = 'example-graph', component_property='figure'),
        [Input(component_id= 'xradioitem', component_property='value'),
         Input(component_id= 'yradioitem', component_property='value')]
        )

    def update_graph(x_axis, y_axis):
        dff=df2
        barchart = px.bar(
            data_frame=dff,
            x=dff['date'],
            y=dff['sales'],
            color='region',
        )
        return barchart
    

    app.run_server(debug=True)

if __name__ == "__main__":
    main()
    