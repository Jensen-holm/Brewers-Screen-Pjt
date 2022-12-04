from views.vis import plot


def result(tbl, player_name, pos_page):
    """
    When the user sends a post request to view player data
    :param tbl: player's subset of the dataframe
    :param player_name: the players name
    :param pos_page: the current page we are viewing ("Pitcher" or "Batter")
    :return: data to go into the index.html template
    """
    plyr_sub = tbl.subset_data(pos_page, player_name)
    plot(plyr_sub.df(), pos_page)
    return (
        plyr_sub.display_tbl(),
        plyr_sub.display_cols(),
        tbl.unique(pos_page),
        plyr_sub.df().at[0, pos_page + "Team"],
        plyr_sub.df().at[0, pos_page + "Side"]
    )
