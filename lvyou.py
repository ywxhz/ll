# -- coding: UTF-8
from flask import Flask, render_template, request, jsonify, json
from flask_bootstrap import Bootstrap
from DataService import DataServicec
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

app = Flask(__name__)
Bootstrap(app)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
db = DataServicec()

@app.route('/seach/<id>')
def view_day(id):
    datas = db.QueryInfoByJID(id)
    return render_template('seach.html', proId = id, lyproject = datas["lyproject"], lyday = datas["lyday"], lypoint = datas["lypoint"])

@app.route('/mobile/<id>')
def view_mobile(id):
    datas = db.QueryInfoByJID(id)
    return render_template('mobile.html', proId = id, lyproject = datas["lyproject"], lyday = datas["lyday"], lypoint = datas["lypoint"])

@app.route('/view')
def view_travel():
    items = db.QueryProjectByName("")
    return render_template('view.html', items = items)

@app.route('/do_search_travel',methods=['POST'])
def search_travel():
    reslut = ""
    if request.method == 'POST':
        val = request.form["val"]
        items = db.QueryProjectByName(val)
        if len(items) > 0:
            reslut = render_template('list-project.html', items = items)
    return reslut

@app.route('/do_createTravel',methods=['POST'])
def create_travel():
    reslut = None
    if request.method == 'POST':
        reslut = db.NewProject(request.form)
    return jsonify(reslut)

@app.route('/qruey_xzq',methods=['POST'])
def qruey_xzq():
    reslut = None
    if request.method == 'POST':
        reslut = db.Queryxzq()
    return jsonify(reslut)

@app.route('/do_editTravel/<id>',methods=['POST'])
def edit_travel(id):
    reslut = {"val": -1}
    if request.method == 'POST':
        reslut["val"] = db.EidtProject(id, request.form)
    return jsonify(reslut)

@app.route('/do_delTravel/<id>',methods=['POST'])
def del_travel(id):
    reslut = None
    if request.method == 'POST':
        reslut = db.DelProject(id)
    return jsonify(reslut)

@app.route('/do_addDay',methods=['POST'])
def add_Day():
    reslut = {}
    if request.method == 'POST':
        jid = request.form["proId"]
        daynum = request.form["daynum"]
        dayId = db.NewdDay(jid, request.form)
        reslut["id"] = dayId
        if dayId > 0:
            day_str = u" 第"+str(daynum)+u"天"
            reslut["list-day"] = render_template('list-day.html', itemDay=reslut, day_active="active", day_str = day_str)
            reslut["list-day-tab"] = render_template('list-day-tab.html', itemDay=reslut, day_active="active", day_str = day_str)
        return jsonify(reslut)

@app.route('/do_delDay',methods=['POST'])
def del_Day():
    reslut = None
    if request.method == 'POST':
        did = request.form["dayId"]
        reslut = db.DelDay(did)
    return jsonify(reslut)

@app.route('/do_editDay',methods=['POST'])
def edit_Day():
    reslut = 0
    vals = request.form.to_dict()
    print vals
    ids = vals['id']
    del (vals['id'])
    # vals.pop(id)
    if request.method == 'POST':
        reslut = db.EidtDay(ids, vals)
    return jsonify(reslut)

@app.route('/do_addPoint',methods=['POST'])
def add_Point():
    reslut = {}
    if request.method == 'POST':
        dayId = request.form["dayId"]
        pId = db.NewPoint(dayId, request.form)
        tempData = request.form.to_dict()
        tempData["id"] = pId
        if pId > 0:
            tempData["list-Point"] = render_template('list-point.html', itemPoint=tempData)
            reslut = tempData
        return jsonify(reslut)

@app.route('/do_delPoint',methods=['POST'])
def del_Point():
    reslut = None
    if request.method == 'POST':
        pointId = request.form["pointId"]
        reslut = db.DelPoint(pointId)
    return jsonify(reslut)

@app.route('/do_editPoint',methods=['POST'])
def edit_Point():
    reslut = 0
    vals=request.form.to_dict()
    print vals
    ids=vals['id']
    del(vals['id'])
    if vals.has_key('transport') and vals.has_key('trtime') and vals.has_key('trevent') and vals.has_key('trdistance'):
        vals['treventds']= u"乘坐"+vals['transport']+u"，花费"+vals['trtime']+u"，距离"+vals['trdistance']+u"需要注意的是："+vals['trevent']
    if request.method == 'POST':
        reslut = db.EidtPoint(ids, vals)
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
    app.run(host='192.168.3.66')
