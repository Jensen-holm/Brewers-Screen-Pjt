from views.vis import plot


def default(tbl, pos_page) -> tuple[str, any, any, any, str, str]:
    """
    :return: default data for the index.html page to be shown before user
    chooses a player to subset
    """
    player_name: str = f"{tbl.df().at[0, 'BatterTeam']} " \
                       f"@ " \
                       f"{tbl.df().at[0, 'PitcherTeam']}"
    plot(tbl.df(), pos_page)
    return (
        player_name,
        tbl.display_cols(),
        tbl.display_tbl(),
        tbl.unique(pos_page),
        "default",
        ""
    )
