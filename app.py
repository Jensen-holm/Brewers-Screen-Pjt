from flask import Flask, render_template, request
import os
from views.table import tbl
from views.vis import plot
from routes.default import default
from routes.result import result

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

    # default data
    pos_page: str = check_page(request.path)
    player_name, headers, data, unique_players = default(tbl, pos_page)

    # when user inputs a pitcher
    if request.method == "POST":
        pos_page: str = check_page(request.path)
        player_name = request.form["player_name_input"].strip()

        data, headers, unique_players = result(
            tbl,
            player_name,
            pos_page
        )

    return render_template(
        "index.html",
        pos_page=pos_page,
        headers=headers,
        data=data,
        player_name=player_name,
        unique_players=unique_players,
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        debug=True,
        port=int(os.environ.get("PORT", 3000))
    )
