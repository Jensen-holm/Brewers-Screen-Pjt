import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import math


def in_2_ft(inches: float) -> float:
    return inches / 12.0


def k_zone(player_df: pd.DataFrame, ax: plt.axis, color_by: str = "TaggedPitchType", title: str = "",
           cp: str = "deep") -> None:
    """
    Strike zone dimensions are according to the pitch-grader
    universal strike zone (https://www.baseballprospectus.com/news/article/40891/prospectus-feature-the-universal-strike-zone/)
    :param player_df:
    :param ax: list of axes to plot on, for the k zone we want to use the first one
    :param color_by: variable in which to color the ball locations by
    :param title: title of the sub-plot
    :param cp: seaborn color palette
    :return: adds the k_zone plot to the given subplot
    """

    sns.color_palette(cp)

    sns.scatterplot(
        player_df,
        x="PlateLocSide",
        y="PlateLocHeight",
        hue=color_by,
        ax=ax,
        s=100
    )
    ax.set_xlim(-2.25, 2.25)
    ax.set_ylim(-1, 5.25)
    ax.title.set_text(title)

    # plotting strike zone rectangle
    sz_left_max = -in_2_ft((19.94 / 2))
    sz_right_max = math.fabs(sz_left_max) * 2
    sz_height = in_2_ft(25.79)
    sz_bottom = in_2_ft(18.29)

    ax.add_patch(
        plt.Rectangle(
            (sz_left_max, sz_bottom),
            sz_right_max,
            sz_height,
            fc="none",
            ec="red"
        )
    )
