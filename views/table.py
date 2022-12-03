import pandas as pd
from pandas import Index
import numpy as np
from data.fp import path_to_data as fp
from dataclasses import dataclass, field
from views.cols import display_cols


@dataclass
class TrackmanData:
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

    def subset_data(self, col: str, val):
        assert (col in self.cols())
        return TrackmanData(_df=self.df()[self.df()[col] == val].reset_index())

    def unique(self, col) -> list:
        assert (col in self.cols())
        return self.df()[col].unique().tolist()

    @staticmethod
    def display_cols() -> list[str]:
        return display_cols

    def display_tbl(self):
        return self.df()[self.display_cols()].to_numpy()


tbl = TrackmanData()
tbl.read()
