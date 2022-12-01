from flask import Flask, render_template, request
import os
from views.table import tbl
from views.vis import plot

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)


@app.route("/result")
@app.route("/hitters")
@app.route("/", methods=["GET", "POST"])
def data_table():

    pos_page = "Pitcher"
    if "hitters" in request.path:
        pos_page = "Batter"

    # default data
    player_name: str = "Texas vs. Arkansas"
    headers = tbl.cols()
    data = tbl.data()
    unique_players = tbl.unique(pos_page)

    # default plot
    plt_data = tbl.df()
    plot(plt_data, default=True)

    if request.method == "POST":
        unique_players = tbl.unique(pos_page)
        player_name = request.form["player_name"].strip()
        plyr_sub = tbl.subset_hitter(player_name)
        data = plyr_sub.to_numpy()
        headers = plyr_sub.columns

    return render_template(
        "index.html",
        pos_page=pos_page,
        headers=headers,
        data=data,
        player_name=player_name,
        unique_players=unique_players
    )


# @app.route("/result", methods=["GET", "POST"])
def plot_page():

    player_name = "Texas vs. Arkansas"

    if request.method == "POST":
        player_name = request.form["player_name"].strip()
        plyr_tbl = tbl.subset_pitcher(player_name)
        plot(plyr_tbl, default=False)

    # then the html will render the saved plot
    return render_template(
        "player_result.html",
        player_name=player_name,
        headers=plyr_tbl.columns,
        data=tbl.subset_pitcher(player_name).to_numpy()
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        debug=True,
        port=int(os.environ.get("PORT", 3000))
    )
