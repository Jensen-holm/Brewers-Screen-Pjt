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


def k_zone(player_df: pd.DataFrame, ax) -> None:
    """
    Strike zone dimensions are according to the pitch-grader
    universal strikezone (https://www.baseballprospectus.com/news/article/40891/prospectus-feature-the-universal-strike-zone/)
    :param player_df:
    :param ax: list of axes to plot on, for the k zone we want to use the first one
    :return:
    """

    def in_2_ft(inches: float) -> float:
        return inches / 12

    sns.scatterplot(
        player_df,
        x="PlateLocSide",
        y="PlateLocHeight",
        hue="TaggedPitchType",
        ax=ax
    )
    ax.set_xlim(-2.25, 2.25)
    ax.set_ylim(-1, 5.25)

    # plotting strike zone rectangle
    sz_left_max = -in_2_ft((19.94 / 2))
    sz_right_max = math.fabs(sz_left_max) * 2
    sz_height = in_2_ft(25.79)
    sz_bottom = in_2_ft(18.29)
    ax.add_patch(plt.Rectangle((sz_left_max, sz_bottom), sz_right_max, sz_height, fc="none", ec="red"))
    # plt.setp(ax.get_legend().get_texts(), fontsize="7")
    # plt.setp(ax.get_legend().get_title(), fontsize="7")


# a pitcher only plot
def spin_vs_mph(pitcher_df: pd.DataFrame, ax) -> None:
    sns.scatterplot(
        pitcher_df,
        x="RelSpeed",
        y="SpinRate",
        hue="TaggedPitchType"
    )
    ax.set_xlim(60, 100)
    ax.set_ylim(1500, 3500)


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

    # use the default argument to determine what should be colored
    # on the plot
