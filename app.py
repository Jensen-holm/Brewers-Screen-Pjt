from flask import Flask, render_template, send_from_directory
from views.table import data_table, CSV
from views.vis import plot_player
import os

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)


@app.route("/")
def main():
    return data_table()


@app.route("/plots")
def plots():
    return render_template(
        "vis.html"
    )


@app.route("/plotresult")
def plot_result():
    # create the players plot and save it into the /views/plots folder
    # the ui will display it in the middle of the screen

    d = CSV()
    d.read()
    plot_player("Dallas, Micah", data=d.df())

    return render_template(
        "player_result.html",
        # add plots and stuff to insert into the template
        player_name="Dallas, Micah",
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        debug=True,
        port=4000
    )
