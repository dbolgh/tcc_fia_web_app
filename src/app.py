import dash
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div("This is my first static web app")


if __name__ == "__main__":
    app.run_server(debug=True)
