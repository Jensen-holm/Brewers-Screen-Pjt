from views.table import TrackmanData
from dataclasses import dataclass
import pandas as pd


@dataclass
class Player:
    _name: str
    _pos: str
    _team: str
    _df: TrackmanData

    def name(self) -> str:
        return self._name

    def pos(self) -> str:
        return self._pos

    def df(self) -> pd.DataFrame:
        return self._df.df()
