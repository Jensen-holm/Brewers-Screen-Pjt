from views.vis import plot


# use filter param to decide which dataframe to show on the table,
# maybe map it to a button on the page

def default(tbl, pos_page):
    """
    :return:
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
