from flask import render_template
import pandas as pd
from pandas import Index
import numpy as np
from data.fp import path_to_data as fp
from dataclasses import dataclass, field


@dataclass
class CSV:
    _path: str = fp
    _df: pd.DataFrame = field(
        default_factory=lambda: pd.DataFrame()
    )

    def path(self) -> str:
        return self._path

    def read(self) -> None:
        self._df = pd.read_csv(self.path())

    def df(self) -> pd.DataFrame:
        return self._df

    def cols(self) -> Index:
        return self.df().columns

    def data(self) -> np.array:
        return self.df().to_numpy()


tbl = CSV()
tbl.read()
