import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
from static.plots.plot import path_2_plots
import pandas as pd

# set plot themes
sns.set()
matplotlib.use("svg")
# COLOR = "F5F5DCFF"
# matplotlib.rcParams['axes.labelcolor'] = COLOR
# matplotlib.rcParams['xtick.color'] = COLOR
# matplotlib.rcParams['ytick.color'] = COLOR


def k_zone(player_df: pd.DataFrame, ax) -> None:
    sns.scatterplot(
        player_df,
        x="PlateLocSide",
        y="PlateLocHeight",
        hue="TaggedPitchType",
        ax=ax[0]
    )
    ax[0].set_xlim(-3, 3)
    ax[0].set_ylim(-2, 7)


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
