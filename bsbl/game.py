from dataclasses import dataclass
import pandas as pd
from team import Team


@dataclass
class Game:
    teams: list[Team]


@dataclass
class Pitch:
    _row: pd.DataFrame
