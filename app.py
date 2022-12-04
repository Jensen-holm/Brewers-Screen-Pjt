from flask import Flask, render_template, request, url_for, redirect
from views.table import tbl
from routes.default import default
from routes.result import result
import pandas as pd
import os

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

app.config["UPLOAD_FOLDER"] = os.getcwd() + "/data/"


@app.route("/pitchers", methods=["GET"])
@app.route("/hitters", methods=["GET"])
@app.route("/hitter_result", methods=["GET", "POST"])
@app.route("/pitcher_result", methods=["GET", "POST"])
def index():
    """
    Main function for the index.html template
    Takes no arguments, most of the logic handling
    requests is inside the routes' module
    :return index.html file with data depending on user:
    """

    def check_page(path: request.path):
        return "Batter" if "hitter" in path else "Pitcher"

    # default data
    pos_page: str = check_page(request.path)

    (player_name, headers,
     data, unique_players,
     plyr_team
     ) = default(tbl, pos_page)

    # when user inputs a player name
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


@app.route("/", methods=["GET", "POST"])
@app.route("/pitchers_custom", methods=["GET", "POST"])
@app.route("/hitters_custom", methods=["GET", "POST"])
def home():
    """
    Renders home.html file, serves as the home page with a data
    dictionary as well as a few notes
    :return home.html:
    """
    return render_template(
        "home.html",
        success="team photos will only be shown for default csv",
        available_games=[]
    )


def allowed_file(file_name: str) -> bool:
    return True


@app.route("/update_db", methods=["POST"])
def upload_csv():
    uploaded_file = request.files["file"]

    if allowed_file(uploaded_file.filename):
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], uploaded_file.filename)
        uploaded_file.save(file_path)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        debug=True,
        port=int(os.environ.get("PORT", 3000))
    )
