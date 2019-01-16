from flask import Flask
from flask import render_template
from app.mdisplay.mdisplay import md2html

app = Flask(__name__)


@app.route('/main')
def main():
    content = md2html('static/mdfile/main.md')
    return render_template('markdown.html', **locals())


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
