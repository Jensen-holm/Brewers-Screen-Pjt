from static.plots.plot import path_2_plots
from views.plots.k_zone import k_zone
from views.plots.spd_vs_spin import spin_vs_mph
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib

# set plot themes
sns.set()
matplotlib.use("svg")


# COLOR = "F5F5DCFF"
# matplotlib.rcParams['axes.labelcolor'] = COLOR
# matplotlib.rcParams['xtick.color'] = COLOR
# matplotlib.rcParams['ytick.color'] = COLOR


def save_plot(fig) -> None:
    fig.savefig(path_2_plots + "player_result_plot.svg")


def plot(player_df, player_pos: str) -> None:
    fig, ax = plt.subplots(1, 3)

    # fig.patch.set_facecolor("#555555")
    fig.set_figheight(8)
    fig.set_figwidth(24)

    k_zone(player_df, ax=ax[0], title="Strike Zone w/ Pitch Type")
    k_zone(player_df, ax=ax[1], color_by="TaggedHitType", title="Strike Zone w/ Hit Type")

    # if it's a pitcher
    if player_pos == "Pitcher":
        spin_vs_mph(player_df, ax[2])
    elif player_pos == "Batter":
        print("batter plt")
    save_plot(fig)
