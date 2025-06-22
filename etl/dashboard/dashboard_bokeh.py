
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, Select
from bokeh.plotting import figure, curdoc
import pandas as pd

# Chargement des données
df = pd.read_csv("data\offres_data_scientist.csv")
df["entreprise"] = df["entreprise"].fillna("Inconnue")
df["contrat"] = df["contrat"].fillna("Non spécifié")
df["lieu"] = df["lieu"].fillna("Non spécifié")

# Fonction pour obtenir les données filtrées
def get_filtered_data(entreprise):
    filtered = df[df["entreprise"] == entreprise]
    contrats = filtered["contrat"].value_counts()
    lieux = filtered["lieu"].value_counts()
    return {
        "contrats": {"x": list(contrats.index), "top": list(contrats.values)},
        "lieux": {"x": list(lieux.index), "top": list(lieux.values)}
    }

# Initialisation avec la première entreprise
initial_entreprise = df["entreprise"].unique()[0]
data = get_filtered_data(initial_entreprise)

source_contrat = ColumnDataSource(data["contrats"])
source_lieu = ColumnDataSource(data["lieux"])

# Graphiques
p1 = figure(x_range=data["contrats"]["x"], title="Répartition des types de contrat", height=300, width=500)
p1.vbar(x="x", top="top", source=source_contrat, width=0.9)

p2 = figure(x_range=data["lieux"]["x"], title="Répartition des offres par lieu", height=300, width=500)
p2.vbar(x="x", top="top", source=source_lieu, width=0.9)

# Sélecteur
entreprises = sorted(df["entreprise"].unique())
select = Select(title="Entreprise :", value=initial_entreprise, options=entreprises)

# Callback
def update(attr, old, new):
    data = get_filtered_data(select.value)
    source_contrat.data = data["contrats"]
    source_lieu.data = data["lieux"]
    p1.x_range.factors = data["contrats"]["x"]
    p2.x_range.factors = data["lieux"]["x"]

select.on_change("value", update)

# Layout final
layout = column(select, row(p1, p2))
curdoc().add_root(layout)
curdoc().title = "Dashboard Bokeh - Offres Data Scientist"
