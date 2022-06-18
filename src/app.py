import os

from flask import Flask, render_template

from engine import MainClass

root_dir = os.path.dirname(os.path.abspath(__file__))
template_folder = os.path.join(root_dir, "templates")
static_directory = os.path.join(template_folder, "static")

app = Flask(__name__, template_folder=template_folder, static_folder=static_directory)

engine_api = MainClass()


@app.route('/', methods=['GET'])
def main():
    columns = engine_api.get_columns_w_ruble()
    context = dict(titles=columns[:1], values=columns[1:])
    engine_api.update_table(columns)
    return render_template("index.html", **context)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
