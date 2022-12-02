import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
from static.plots.plot import path_2_plots
import pandas as pd
from k_zone import k_zone
from spd_vs_spin import spin_vs_mph

# set plot themes
sns.set()
matplotlib.use("svg")


# COLOR = "F5F5DCFF"
# matplotlib.rcParams['axes.labelcolor'] = COLOR
# matplotlib.rcParams['xtick.color'] = COLOR
# matplotlib.rcParams['ytick.color'] = COLOR


def save_plot(fig) -> None:
    fig.savefig(path_2_plots + "player_result_plot.svg")


def plot(player_df: pd.DataFrame, player_pos: str) -> None:
    fig, ax = plt.subplots(1, 2)

    # fig.patch.set_facecolor("#555555")
    fig.tight_layout(pad=2.0)
    fig.set_figheight(8)
    fig.set_figwidth(12)

    k_zone(player_df, ax=ax[0])

    # if it's a pitcher
    if player_pos == "Pitcher":
        spin_vs_mph(player_df, ax[1])
    elif player_pos == "Batter":
        print('batter plot')

    save_plot(fig)
