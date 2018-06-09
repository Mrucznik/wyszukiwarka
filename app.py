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


@app.route('/findWord/<string:word>')
def find_word(word):
    i = 1
    while 1:
        print('requst to get file ' + str(i))
        r = http.request('GET', 'www.gutenberg.org/files/{0}/{0}.txt'.format(i))
        if r.status != 200:
            print('Error ' + str(r.status))
        else:
            print('searching in file ' + str(i))
            if word in str(r.data):
                return 'www.gutenberg.org/files/{0}/{0}.txt'.format(i)
        i += 1


if __name__ == '__main__':
    app.run()
