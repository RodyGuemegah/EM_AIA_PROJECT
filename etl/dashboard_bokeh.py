from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, Select, Div
from bokeh.layouts import column, row
from bokeh.plotting import figure
import pandas as pd

# Chargement des données
df = pd.read_csv("data/offres_data_scientist.csv")

# Nettoyage (si jamais il y a des NaN dans les colonnes clés)
df = df.dropna(subset=["entreprise", "lieu", "contrat"])

# Entreprises disponibles
entreprises = df["entreprise"].unique().tolist()
entreprise_select = Select(title="Entreprise :", value=entreprises[0], options=entreprises)

# Création des sources vides
source_contrat = ColumnDataSource(data=dict(contrat=[], count=[]))
source_lieu = ColumnDataSource(data=dict(lieu=[], count=[]))

# Graphique 1 : Type de contrat
plot_contrat = figure(x_range=[], height=300, title="Répartition des types de contrat")
bar_contrat = plot_contrat.vbar(x="contrat", top="count", source=source_contrat, width=0.6)

# Graphique 2 : Lieu
plot_lieu = figure(x_range=[], height=300, title="Répartition des offres par lieu")
bar_lieu = plot_lieu.vbar(x="lieu", top="count", source=source_lieu, width=0.6)

# Fonction de mise à jour
def update(attr, old, new):
    selected = entreprise_select.value
    df_selected = df[df["entreprise"] == selected]

    contrat_count = df_selected["contrat"].value_counts()
    lieu_count = df_selected["lieu"].value_counts().head(10)  # Top 10 lieux

    # MAJ data
    source_contrat.data = {
        "contrat": contrat_count.index.tolist(),
        "count": contrat_count.values.tolist()
    }
    source_lieu.data = {
        "lieu": lieu_count.index.tolist(),
        "count": lieu_count.values.tolist()
    }

    # MAJ x_range
    plot_contrat.x_range.factors = contrat_count.index.tolist()
    plot_lieu.x_range.factors = lieu_count.index.tolist()

# Initialisation
update(None, None, None)
entreprise_select.on_change("value", update)

# Titre du dashboard
titre = Div(text="<h1 style='text-align:center'>📊 Dashboard Bokeh - Offres Data Scientist</h1>")

# Layout
layout = column(titre, entreprise_select, row(plot_contrat, plot_lieu))
curdoc().add_root(layout)
