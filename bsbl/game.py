from dataclasses import dataclass, field
from views.table import CSV
import pandas as pd
from team import Team


@dataclass
class Game:
    teams: list[Team]


@dataclass
class Pitch:
    _row: pd.DataFrame
