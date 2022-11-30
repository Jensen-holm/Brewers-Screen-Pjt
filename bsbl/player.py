from dataclasses import dataclass, field

import pandas as pd


@dataclass
class Player:
    _name: str

    # will contain all the rows from the dataframe
    # in which the player was either the hitter or the pitcher
    _rows: pd.DataFrame = field(
        default_factory=lambda: pd.DataFrame()
    )

    def name(self) -> str:
        return self._name


class Hitter(Player):

    def probs(self):
        return


class Pitcher(Player):

    def probs(self):
        return
