import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
from static.plots.plot import path_2_plots
import pandas as pd
import math

# set plot themes
sns.set()
matplotlib.use("svg")


# COLOR = "F5F5DCFF"
# matplotlib.rcParams['axes.labelcolor'] = COLOR
# matplotlib.rcParams['xtick.color'] = COLOR
# matplotlib.rcParams['ytick.color'] = COLOR

def in_2_ft(inches: float) -> float:
    return inches / 12


def k_zone(player_df: pd.DataFrame, ax) -> None:
    """
    Strike zone dimensions are according to the pitch-grader
    universal strikezone (https://www.baseballprospectus.com/news/article/40891/prospectus-feature-the-universal-strike-zone/)
    :param player_df:
    :param ax:
    :return:
    """
    sns.scatterplot(
        player_df,
        x="PlateLocSide",
        y="PlateLocHeight",
        hue="TaggedPitchType",
        ax=ax[0]
    )
    ax[0].set_xlim(-2.25, 2.25)
    ax[0].set_ylim(-1, 5)

    # plotting strike zone rectangle
    sz_left_max = -in_2_ft((19.94 / 2))
    sz_right_max = math.fabs(sz_left_max) * 2
    sz_height = in_2_ft(25.79)
    sz_bottom = in_2_ft(18.29)
    ax[0].add_patch(plt.Rectangle((sz_left_max, sz_bottom), sz_right_max, sz_height, fc="none", ec="red"))


def save_plot(fig) -> None:
    fig.savefig(path_2_plots + "player_result_plot.svg")


def plot(player_df: pd.DataFrame, default: bool) -> None:
    fig, ax = plt.subplots(1, 2)

    # fig.patch.set_facecolor("#000000")
    fig.set_figheight(4)
    fig.set_figwidth(6)

    k_zone(player_df, ax=ax)
    save_plot(fig)

    # use the default argument to determine what should be colored
    # on the plot
