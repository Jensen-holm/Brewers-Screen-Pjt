import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
from views.table import CSV
from views.plots.plots import path_to_plots

# from bsbl.player import Player

# set default themes to seaborn
sns.set()
matplotlib.use("svg")


def plot_player(player_name, data):
    # subset the data to just get the player

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(x="PlateLocSide", y="PlateLocHeight", data=data)
    save_plot(fig)


def save_plot(plot, name: str = "player_result_plot"):
    plot.savefig(path_to_plots + "/" + name)


if __name__ == "__main__":
    # use this plot to debug how our plot works and looks
    d = CSV()
    d.read()
    plot_player("Dallas, Micah", data=d.df())
