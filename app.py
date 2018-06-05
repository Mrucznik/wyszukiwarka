from flask import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    try:
        return render_template("index.html")
    except Exception as e:
        return "Błąd"


if __name__ == '__main__':
    app.run()
