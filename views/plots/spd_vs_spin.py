import seaborn as sns


def spin_vs_mph(pitcher_df, ax, title="Spin Rate vs. MPH") -> None:
    """
    Plots a pitchers spin rate versus the release speed of the ball
    grouped by the tagged type of the pitch
    :param pitcher_df: pitchers' subset of the data
    :param ax: the subplot we want to put this graph on
    :param title: the title of the plot
    :return: adds the plot to the given subplot
    """
    sns.scatterplot(
        pitcher_df,
        x="RelSpeed",
        y="SpinRate",
        hue="TaggedPitchType",
        s=100
    )
    ax.set_xlim(60, 100)
    ax.set_ylim(900, 3500)
    ax.title.set_text(title)
