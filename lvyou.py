from flask import Flask, render_template, request, jsonify, json
from flask_bootstrap import Bootstrap
from DataService import DataServicec

app = Flask(__name__)
Bootstrap(app)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
db = DataServicec()

@app.route('/seach/<id>')
def seach_travel(id):
    datas = db.QueryInfoByJID(id)
    return render_template('seach.html', proId = id)

@app.route('/view')
def view_travel():
    items = db.QueryProjectByName("")
    return render_template('view.html', items = items)

@app.route('/do_createTravel',methods=['POST'])
def create_travel():
    reslut = {}
    if request.method == 'POST':
        reslut = db.NewProject(request.form)
    return jsonify(reslut)

@app.route('/do_editDay',methods=['POST'])
def edit_Day():
    reslut = {}
    print  request.form
    if request.method == 'POST':
        reslut = db.EidtPoint(11,request.form)
    return jsonify(reslut)

@app.route('/do_delTravel/<id>',methods=['POST'])
def del_travel(id):
    reslut = None;
    if request.method == 'POST':
        reslut = db.DelProject(id)
    return jsonify(reslut)

@app.route('/do_addDay',methods=['POST'])
def add_Day():
    reslut = None
    if request.method == 'POST':
        jid = request.form["proId"]
        reslut = db.NewdDay(jid, request.form)
    return jsonify(reslut)

@app.route('/do_delDay',methods=['POST'])
def del_Day():
    reslut = None
    if request.method == 'POST':
        did = request.form["dayId"]
        reslut = db.DelDay(did)
    return jsonify(reslut)




@app.route('/test')
def hello_world1():
    return render_template('test.html')


@app.route('/user/<name>')
def user(name):
    return render_template('test.html', name=name)

@app.route('/test')
def hello_world1111():
    return render_template('test.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
