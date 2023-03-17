from flask import Flask, render_template, request, url_for, redirect
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<string:page_name>')
def page_route(page_name):
    return render_template(page_name)


@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}


if __name__ == '__main__':
    app.debug = True
    app.run()
