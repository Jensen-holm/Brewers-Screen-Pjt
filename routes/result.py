from views.vis import plot


def result(tbl, player_name, pos_page):
    """
    When the user sends a post request to view player data
    :param tbl:
    :param player_name:
    :param pos_page:
    :return:
    """
    unique_players = tbl.unique(pos_page)
    plyr_sub = tbl.subset_data(pos_page, player_name)
    data = plyr_sub.to_numpy()
    headers = plyr_sub.columns
    plot(plyr_sub, default=False)
    return (
        data,
        headers,
        unique_players
    )
