import matplotlib.pyplot as plt
import seaborn as sns
from bsbl.player import Player

# set default themes to seaborn
sns.set()


def plot_player(player: Player):
    return


def save_plot(plot, name: str):
    plot.savefig("plots/" + name + ".png")
