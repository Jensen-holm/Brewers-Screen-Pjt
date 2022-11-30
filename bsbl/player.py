from dataclasses import dataclass


@dataclass
class Player:
    name: str


class Hitter(Player):

    def probs(self):
        return


class Pitcher(Player):

    def probs(self):
        return
