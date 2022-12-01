import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
from static.plots.plot import path_2_plots
import pandas as pd


# set default themes to seaborn
sns.set()
matplotlib.use("svg")


def k_zone(player_df: pd.DataFrame, ax) -> None:
    print(player_df)
    ax[0, 0].scatter(
        player_df["PlateLocSide"],
        player_df["PlateLocHeight"]
    )

    ax[0, 0].set_title("K Zone")


def save_plot(fig) -> None:
    fig.savefig(path_2_plots + "player_result_plot.svg")


def plot(player_df: pd.DataFrame) -> None:
    fig, ax = plt.subplots(2, 2)
    k_zone(player_df, ax=ax)

    save_plot(fig)
