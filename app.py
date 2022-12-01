from flask import Flask, render_template
from views.table import data_table

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)


@app.route("/", methods=["GET"])
def main():
    return data_table()


@app.route("/plots", methods=["GET"])
def plots():
    return render_template(
        "vis.html"
    )


@app.route("/plotresult", methods=["GET", "POST"])
def plot_result():
    # recieve the post request, find the player
    # and then plot that players pitch data and place it into the template
    return render_template(
        "player_result.html",
        # add plots and stuff to insert into the template
        player_name="Jensen Holm"
    )


if __name__ == "__main__":
    app.run(
        debug=True,
        port=4000
    )
