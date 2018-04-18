from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True

@app.route('/seach')
def hello_world():
    return render_template('seach.html')

@app.route('/test')
def hello_world1():
    return render_template('test.html')

@app.route('/test')
def user(name):
    return render_template('test.html', name=name)

@app.route('/test')
def hello_world1111():
    return render_template('test.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
