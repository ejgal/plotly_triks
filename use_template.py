import pandas as pd
import plotly.express as px
import plotly.io as pio

import nav_template

pio.templates.default = "nav"

print(pio.templates.default)
print(pio.templates["nav"])


def basefig(fig):
    fig.layout.xaxis.title = "Tittel x-akse"
    fig.layout.yaxis.title = "Tittel y-akse"
    fig.layout.title = "Tittel"
    fig.layout.legend.title = "Tittel legend"
    return fig


if __name__ == "__main__":
    df = pd.read_csv("data/datasett.csv", index_col=0)
    df = df.set_index(pd.DatetimeIndex(df.index))
    df = df.resample("W-MON", label="left", closed="left").sum()

    # bar
    for template in ["nav", "plotly"]:
        fig = px.bar(df, template=template)
        fig = basefig(fig)
        fig.write_image(f"figur/bar_{template}.png")

    # line
    for template in ["nav", "plotly"]:
        fig = px.line(df, template=template)
        fig = basefig(fig)
        fig.write_image(f"figur/line_{template}.png")

    # scatter
    for template in ["nav", "plotly"]:
        fig = px.scatter(df, template=template)
        fig = basefig(fig)
        fig.write_image(f"figur/scatter_{template}.png")

    # area
    for template in ["nav", "plotly"]:
        fig = px.area(df, template=template)
        fig = basefig(fig)
        fig.write_image(f"figur/area_{template}.png")

    # 2d scatter
    for template in ["nav", "plotly"]:
        fig = px.scatter(df, x="Første", y="Andre", color="Tredje", template=template)
        fig = basefig(fig)
        fig.write_image(f"figur/2dscatter_{template}.png")
