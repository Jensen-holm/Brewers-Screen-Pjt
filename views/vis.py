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
    fig.savefig(path_2_plots + "player_result_plot.svg")


def plot(player_df, player_pos: str) -> None:
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
