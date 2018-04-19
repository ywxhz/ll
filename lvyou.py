from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap
from DataService import DataServicec

app = Flask(__name__)
Bootstrap(app)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
db = DataServicec()

@app.route('/seach')
def hello_world():
    return render_template('seach.html')

<<<<<<< Updated upstream
@app.route('/test')
def hello_world1():
    return render_template('test.html')

@app.route('/test')
=======
@app.route('/create-travel',methods=['POST'])
def create_travel():
    if request.method == 'POST':
        id = db.NewProject(request.form)
    return jsonify({'id': id})

@app.route('/user/<name>')
>>>>>>> Stashed changes
def user(name):
    return render_template('test.html', name=name)

@app.route('/test')
def hello_world1111():
    return render_template('test.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
