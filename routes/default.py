from views.vis import plot


def default(tbl, pos_page):
    """
    Returns default data for the main route to handle
    :return:
    """
    player_name: str = "Texas vs. Arkansas"
    headers = tbl.cols()
    data = tbl.data()
    unique_players = tbl.unique(pos_page)
    plot(tbl.df(), pos_page)
    plyr_team = "default"
    return (
        player_name,
        headers,
        data,
        unique_players,
        plyr_team
    )
