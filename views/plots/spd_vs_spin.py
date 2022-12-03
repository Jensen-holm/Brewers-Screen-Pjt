import seaborn as sns


# a pitcher only plot
def spin_vs_mph(pitcher_df, ax, title="Spin Rate vs. MPH") -> None:
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
