from flask import *
import urllib3
app = Flask(__name__)

http = urllib3.PoolManager()


@app.route('/')
def index():
    try:
        return render_template("index.html")
    except Exception as e:
        return "Błąd"


@app.route('/book/<int:book_id>')
def book(book_id):
    r = http.request('GET', 'www.gutenberg.org/files/{0}/{0}.txt'.format(book_id))
    return r.data


if __name__ == '__main__':
    app.run()
