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


if __name__ == "__main__":
    app.run(
        debug=True,
        port=4000
    )
