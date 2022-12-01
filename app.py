from flask import Flask, render_template, request
import os
from views.table import tbl
from views.vis import plot

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)


@app.route("/")
def data_table():
    return render_template(
        "table.html",
        headers=tbl.cols(),
        data=tbl.data()
    )


@app.route("/plots")
def input():
    return render_template("vis.html")


@app.route("/result", methods=["GET", "POST"])
def plot_page():

    player_name = "Dallas, Micah"

    if request.method == "POST":
        player_name = request.form["fname"]
        plot(tbl.subset_pitcher(player_name))

    # then the html will render the saved plot
    return render_template(
        "player_result.html",
        player_name=player_name
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        debug=True,
        port=int(os.environ.get("PORT", 3000))
    )
