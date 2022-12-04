from static.plots.plot import path_2_plots
from views.plots.k_zone import k_zone
from views.plots.spd_vs_spin import spin_vs_mph
from views.plots.spray_chart import spray_chart
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib

# set plot themes
sns.set()
matplotlib.use("svg")


def save_plot(fig) -> None:
    """
    Saves a given plot into our assets' folder
    :param fig: the matplotlib figure object we want to save
    :return: saved svg of plots in the assets folder
    """
    fig.savefig(path_2_plots + "player_result_plot.svg")


def plot(player_df, player_pos: str) -> None:
    """
    The main function to be run in order to generate
    the 1 x 3 row of graphs based on the current app view
    :param player_df: subset of the data to plot from
    :param player_pos: if the player is a "Pitcher" or "Batter"
    :return: saves the plot as an svg file in our assets folder
    """
    fig, ax = plt.subplots(1, 3)

    fig.set_figheight(8)
    fig.set_figwidth(24)

    k_zone(
        player_df,
        ax=ax[0],
        title="Strike Zone w/ Pitch Type"
    )

    k_zone(
        player_df,
        ax=ax[1],
        color_by="PitchResult",
        title="Strike Zone w/ Result Type",
        cp="icefire"
    )

    if player_pos == "Pitcher":
        spin_vs_mph(player_df, ax[2])
    elif player_pos == "Batter":
        spray_chart(player_df, ax[2])

    save_plot(fig)
