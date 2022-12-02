import seaborn as sns
import pandas as pd


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
