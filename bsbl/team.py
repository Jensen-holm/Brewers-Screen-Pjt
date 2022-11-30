from dataclasses import dataclass, field
from player import Player


@dataclass
class Team:
    players: list[Player] = field(
        default_factory=lambda: []
    )
