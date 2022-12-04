import os
import pandas as pd
import seaborn as sns
import math
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
from PIL import Image


def spray_chart(player_df: pd.DataFrame, ax):
    dist = player_df["Distance"].to_numpy()
    angle = player_df["Bearing"].to_numpy()

    player_df["hc_x"] = [math.fabs(d * math.cos(angle[i])) for i, d in enumerate(dist)]
    player_df["hc_y"] = [math.fabs(d * math.sin(angle[i])) for i, d in enumerate(dist)]
    player_df["events"] = player_df["PlayResult"]

    aff = Image.open(os.getcwd() + "/views/plots/aff.png") \
        .rotate(90 + 180).resize((1500, 1500))
    ax.imshow(aff, extent=(-265, 600, -310, 600))

    sns.scatterplot(
        data=player_df,
        x="hc_x",
        y="hc_y",
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
            ec="brown"
        )
    )
