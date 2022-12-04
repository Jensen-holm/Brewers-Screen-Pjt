from views.vis import plot


def default(tbl, pos_page):
    """
    :return: default data for the index.html page to be shown before user
    chooses a player to subset
    """
    # making it like this so that it will be dynamic if data
    # from a different game were imported, it would show their names
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
