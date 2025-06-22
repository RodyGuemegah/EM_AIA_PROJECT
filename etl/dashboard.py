import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
import os

# Charger les données CSV générées
print(os.path.abspath("etl/output/data_scientist_offres.csv"))
df = pd.read_csv("data\offres_data_scientist.csv")

# Lancer l'app Dash
app = dash.Dash(__name__)
app.title = "Offres d'emploi Data Science"

# Graphique : nombre d'offres par lieu
fig1 = px.bar(df, x="lieu", title="Nombre d'offres par lieu")

# Graphique : type de contrat
fig2 = px.pie(df, names="contrat", title="Répartition des types de contrat")

# Disposition de l'app
app.layout = html.Div([
    html.H1("Dashboard - Offres d'emploi en Data Science"),
    dcc.Graph(figure=fig1),
    dcc.Graph(figure=fig2),
])

if __name__ == '__main__':
    app.run(debug=True)
