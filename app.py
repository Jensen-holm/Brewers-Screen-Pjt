from flask import Flask, render_template, request
import os
from views.table import tbl
from views.vis import plot

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)


@app.route("/", methods=["GET"])
@app.route("/hitters", methods=["GET"])
@app.route("/hitter_result", methods=["GET", "POST"])
@app.route("/pitcher_result", methods=["GET", "POST"])
def index():

    # if this function is removed out of this function it will not work for flask
    def check_page(path: request.path):
        return "Batter" if "hitter" in path else "Pitcher"

    pos_page: str = check_page(request.path)

    # default data
    player_name: str = "Texas vs. Arkansas"
    headers = tbl.cols()
    data = tbl.data()
    unique_players = tbl.unique(pos_page)

    # default plot
    plt_data = tbl.df()
    plot(plt_data, default=True)

    if request.method == "POST":
        pos_page: str = check_page(request.path)
        unique_players = tbl.unique(pos_page)
        player_name = request.form["player_name_input"].strip()
        plyr_sub = tbl.subset_data(pos_page, player_name)
        data = plyr_sub.to_numpy()
        headers = plyr_sub.columns
        plot(plyr_sub, default=False)

    return render_template(
        "index.html",
        pos_page=pos_page,
        headers=headers,
        data=data,
        player_name=player_name,
        unique_players=unique_players
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        debug=True,
        port=int(os.environ.get("PORT", 3000))
    )
