from typing import List
from dataclasses import dataclass
import plotly.graph_objects as go

@dataclass
class IndicatorEntry:
    value: float
    title: str
    row: int = 0
    column: int = 0
    mode: str = "number"
    valueformat: str = ","

    @property
    def kwargs(self):
        kwargs = {}
        kwargs["domain"] = {"column": self.column, "row": self.row}
        kwargs["title"] = {"text": self.title}
        kwargs["mode"] = self.mode
        kwargs["value"] = self.value
        kwargs["number"] = {"valueformat": self.valueformat}
        return kwargs


@dataclass
class Indicator:
    entries: List[IndicatorEntry]
    pattern: str = "independent"
    autosize: bool = True

    @property
    def rows(self):
        return max([entry.row for entry in self.entries]) + 1

    @property
    def columns(self):
        return max([entry.column for entry in self.entries]) + 1

    @property
    def kwargs(self):
        return {}

    @property
    def layout_kwargs(self):
        kwargs = {}
        kwargs["grid"] = {
            "columns": self.columns,
            "rows": self.rows,
            "pattern": self.pattern,
        }
        kwargs["autosize"] = self.autosize
        return kwargs

    def plot(self) -> go.Figure:
        fig = go.Figure()
        for indicator in self.entries:
            fig.add_indicator(**indicator.kwargs)
        fig.update_layout(**self.layout_kwargs)
        return fig



if __name__ == "__main__":
    import pandas as pd
    import plotly.io as pio

    df = pd.DataFrame()
    df["tall"] = pd.Series([1, 2, 3, 4])

    indicators = [
            IndicatorEntry(value=df.tall.max(), title="Max", column=0, row=0),
            IndicatorEntry(value=df.tall.mean(), title="Mean", column=1, row=1),
            IndicatorEntry(value=df.tall.median(), title="Median", column=2, row=2),
            IndicatorEntry(value=df.tall.min(), title="Min", column=0, row=2),
            IndicatorEntry(value=df.tall.sum(), title="Sum", column=2, row=0),
    ]


    fig = Indicator(indicators).plot()
    pio.show(fig)