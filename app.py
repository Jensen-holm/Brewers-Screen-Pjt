from flask import Flask, render_template
import os
from views.table import data_table, CSV
from views.vis import plot_player

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)


@app.route("/")
def index() -> str:
    return data_table()


@app.route("/plots")
def input():
    return render_template("vis.html")


@app.route("/result")
def plot():
    # parse request data and put into plot player function
    d = CSV()
    d.read()
    plot_player("Dallas, Micah", d.df())
    # then teh html will render the saved plot
    return render_template(
        "player_result.html"
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        debug=True,
        port=int(os.environ.get("PORT", 3000))
    )
