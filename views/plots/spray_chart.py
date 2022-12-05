import os
import pandas as pd
import seaborn as sns
import math
import matplotlib.pyplot as plt
from PIL import Image


def spray_chart(player_df: pd.DataFrame, ax: plt.axis) -> None:
    """
    Calculates the coordinates of the landing point of the ball in feet
    and plots it on top of the Milwaukee Brewers field dimensions.
    I understand that I could make the calculation separate from the plotting
    but for the sake of this application I want this calculation to be noticed
    :param player_df: Pandas dataframe containing the players' subset
    :param ax: graph to put the spray chart on
    :return: Nothing
    """
    dist, angle = player_df["Distance"].to_numpy(), player_df["Direction"].to_numpy()

    player_df["hit_coords_x"] = [math.fabs(d * math.cos(angle[i])) for i, d in enumerate(dist)]
    player_df["hit_coords_y"] = [math.fabs(d * math.sin(angle[i])) for i, d in enumerate(dist)]

    aff: Image.Image = Image.open(os.getcwd() + "/views/plots/aff.png") \
        .rotate(90 + 180).resize((1500, 1500))
    ax.imshow(aff, extent=(-265, 600, -310, 600))

    sns.scatterplot(
        player_df,
        x="hit_coords_x",
        y="hit_coords_y",
        hue="PlayResult",
        s=100
    )
    ax.set_ylim(-50, 500)
    ax.set_xlim(-50, 500)

    # plot the baseball diamond
    ax.add_patch(
        plt.Rectangle(
            (0, 0),
            90,
            90,
            fc="none",
            ec="red"
        )
    )

    ax.title.set_text("Spray Chart")
