import pandas as pd
import seaborn as sns
import math


def spray_chart(player_df: pd.DataFrame, ax):
    # calculate point on circumference of circle with radius of distance
    dist = player_df["Distance"].dropna().to_numpy()
    angle = player_df["Bearing"].dropna().to_numpy()

    x = [math.fabs(d * math.cos(math.radians(angle[i]))) for i, d in enumerate(dist)]
    y = [math.fabs(d * math.sin(math.radians(angle[i]))) for i, d in enumerate(dist)]
    print(x, y)

    sns.scatterplot(
        x=x,
        y=y
    )
