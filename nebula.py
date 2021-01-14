from flask import Flask, app
from flask.templating import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('nebula.html')


if __name__ == "__main__":
    app.run(debug=True)