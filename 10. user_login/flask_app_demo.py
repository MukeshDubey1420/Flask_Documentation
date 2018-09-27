from flask import Flask

app = Flask(__name__)

@app.route('/<name>')
def index(name):
    return name[1000]


if __name__ == '__main__':
    app.run(debug = True)
