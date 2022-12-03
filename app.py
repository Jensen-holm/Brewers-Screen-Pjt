import pandas as pd
from data.fp import path_to_data
from flask import Flask, render_template, request
from views.table import TrackmanData
from routes.default import default
from routes.result import result
import os

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

app.config["UPLOAD_FOLDER"] = path_to_data.split("/")[:-1]


@app.route("/pitchers", methods=["GET"])
@app.route("/hitters", methods=["GET"])
@app.route("/hitter_result", methods=["GET", "POST"])
@app.route("/pitcher_result", methods=["GET", "POST"])
def index(tbl: TrackmanData = TrackmanData()):
    """
    Main function for the index.html template
    Takes no arguments, most of the logic handling
    requests is inside the routes' module
    :return index.html file with data depending on user:
    """

    tbl.read()

    def check_page(path: request.path):
        return "Batter" if "hitter" in path else "Pitcher"

    # default data
    pos_page: str = check_page(request.path)

    (player_name, headers,
     data, unique_players,
     plyr_team
     ) = default(tbl, pos_page)

    # when user inputs a pitcher
    if request.method == "POST":
        pos_page: str = check_page(request.path)
        player_name = request.form["player_name_input"].strip()
        data, headers, unique_players, plyr_team = result(
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
        plyr_team=plyr_team
    )


ALLOWED_EXTENSIONS: set[str] = {
    "csv"
}


def allowed_file(file):
    return True if file.split(".")[-1] in ALLOWED_EXTENSIONS else False


@app.route("/", methods=["GET", "POST"])
@app.route("/pitchers_custom", methods=["GET", "POST"])
@app.route("/hitters_custom", methods=["GET", "POST"])
def home():
    """
    Renders home.html file, serves as the home page with a data
    dictionary as well as a few notes
    :return home.html:
    """
    if request.method == "POST":
        if "file" not in request.files:
            return render_template(
                "home.html",
                success="No file found in request"
            )
        if not allowed_file(request.form["trackman_csv"]):
            return render_template(
                "home.html",
                success="Invalid file type"
            )

        # if there were no problems, insert the csv into the analysis pages
        # will need to save it into the data folder
        return render_template(
            "index.html",
        )

    return render_template(
        "home.html",
        success="team photos will only be shown for default csv"
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        debug=True,
        port=int(os.environ.get("PORT", 3000))
    )
