import seaborn as sns
import pandas as pd


# a hitter only plot
def la_ev(player_df: pd.DataFrame, ax, title="Exit Velo vs. Launch Angle"):
    sns.scatterplot(
        player_df,
        x="ExitSpeed",
        y="Angle",
        hue="PlayResult",
        s=100
    )
    ax.title.set_text(title)
