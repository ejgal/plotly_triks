import plotly.graph_objects as go
import plotly.io as pio

categorical = (
    "#0067C5",
    "#BA3A26",
    "#06893A",
    "#634689",
    "#FF9100",
    "#66CBEC",
    "#F0C419",
)
sequential = [[0, "#1E3345"], [0.5, "#0067C5"], [1, "#CCE1F3"]]
diverging = [
    [0, "#943425"],
    [0.1, "#BA3A26"],
    [0.5, "#FFFFFF"],
    [0.9, "#06893A"],
    [1, "#0D7034"],
]
new_layout = {
    "colorway": categorical,
    "colorscale": {"diverging": diverging, "sequential": sequential},
    "font": {"family": "Source Sans Pro", "size": 16},
    "hovermode": "x unified",
}


plotly_template = pio.templates["plotly"]


data = {key: plotly_template["data"][key] for key in plotly_template["data"]}
layout = {key: plotly_template["layout"][key] for key in plotly_template["layout"]}


template = {
    "data": data,
    "layout": layout,
}


for key, val in new_layout.items():
    template["layout"][key] = val

pio.templates["nav"] = template
