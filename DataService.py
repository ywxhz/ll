#!/usr/bin/env pytho
# -- coding: UTF-8
from MySqlCon import MySqlconc
import json
import urllib2
import time


class DataServicec:

    def xx(self):
        ms = MySqlconc()
        # sqlstr='INSERT INTO lyproject (id,pname) VALUES (111,\'dfdff\')'
        enum=ms.SQLexecute(' ')
        print enum
        return enum

    def intsettest(self):
        ms = MySqlconc()
        sqlstr='INSERT INTO lyproject (id,pname) VALUES (15,\'速度\')'
        enum=ms.SQLexecute(sqlstr)
        print enum
        return enum

    def qeurytest(self):
        ms = MySqlconc()
        sqlstr = 'SELECT * FROM lyproject'
        enum = ms.SQLcumQuert('lyproject',sqlstr)

    #新建计划 vdct:{'name': '北京7天', 'event': '北京故宫非常好玩，颐和园，长城等地方'};
    # 说明
    # name:计划名称
    # event:计划描述
    #返回值：新增计划的ID
    def NewProject(self,vdct):
        cum='';
        val=''
        for key in vdct:
            cum=cum+key+","
            val=val+"'"+vdct[key] + "',"
            print key+" "+vdct[key]
        cum=cum[:-1];
        val = val[:-1];
        ms = MySqlconc()
        sqlstr = "INSERT INTO lyproject ("+cum+") VALUES ("+val+")"
        print "sqlstr "+sqlstr
        enum = ms.SQLexecute(sqlstr)
        msg=""
        msgval= -1
        if enum == 0:
            msg=ms.getsqlmsg()
        else:
            sqls="select max(id) from lyproject"
            reid=ms.SQLQuery(sqls)
            maxid=0
            for idval in reid:
                for mid in idval:
                    maxid= mid
            print  maxid
            msgval=maxid
        dict = {}
        dict['msg'] = msg
        dict['val'] = msgval

        print str(dict)
        return dict

    # 修改project
    # jid：计划ID
    # ---vdct说明，vdct可以传任意字段
    # name:计划名称
    # event:计划描述
    # 返回值：返回修改的影响的行数
    def EidtProject(self, jid, vdct):
        setval = '';
        for key in vdct:
            setval = setval + key + "='" + vdct[key] + "',"
        setval = setval[:-1];
        ms = MySqlconc()
        sqlstr = "UPDATE lyproject SET " + setval + " where id=" + str(jid)
        print "sqlstr " + sqlstr
        enum = ms.SQLexecute(sqlstr)
        return enum

    # 删除project
    # jid：计划ID
    # 返回值：1 成功，0 失败
    def DelProject(self, jid):
        ms = MySqlconc()
        sqlstr = "DELETE FROM lyproject WHERE id=" + str(jid)
        print "sqlstr " + sqlstr
        enum1 = ms.SQLexecute(sqlstr)
        sqlstr = "DELETE FROM lyday WHERE id in(select did from lyrt where jid=" + str(jid) + ")"
        print "sqlstr " + sqlstr
        enum2 = ms.SQLexecute(sqlstr)
        sqlstr = "DELETE FROM lypoint WHERE id in( select pid from lyrtp where did in (select did from lyrt where jid=" + str(jid) + ")) "
        print "sqlstr " + sqlstr
        enum3 = ms.SQLexecute(sqlstr)
        sqlstr ="DELETE FROM lyrtp WHERE did in(select did from lyrt where jid="+str(jid) +")"
        print "sqlstr " + sqlstr
        enum4 = ms.SQLexecute(sqlstr)
        sqlstr = "DELETE FROM lyrt WHERE jid=" + str(jid)
        print "sqlstr " + sqlstr
        enum5 = ms.SQLexecute(sqlstr)
        return enum1
    # 查询project
    # qv：按照名称或者是内容的模糊检索值
    # 返回值：所有相关的计划信息list包 dict
    def QueryProjectByName(self, qv):
        # Fstr = '';
        # for key in vdct:
        #     Fstr = Fstr + key +" like '%"+vdct[key]+"%' or"
        #     print Fstr
        # Fstr = Fstr[:-2];
        ms = MySqlconc()
        sqlstr = "select * from lyproject where name like '%"+qv+"%' or event like '%"+qv+"%'"
        print "sqlstr " + sqlstr
        return   ms.SQLcumQuert("lyproject",sqlstr)

    #插入day
        # jid：计划ID
        # ---vdct说明 vdct可以传任意字段
        # daynum:第几天
        # name:当天说明
        # 返回值：新增天的ID
    # 根据计划ID查询该计划下所有天数
    # jid：计划ID
    # 返回值：vallist
    # 链表 ，[0]计划信息、[1]天的信息、[2] 景点信息
    def QueryInfoByJID(self, jid):
        vallist = []
        ms = MySqlconc()
        sqlstr = "select * from lyproject where id =" + str(jid)
        print "sqlstr " + sqlstr
        vallist.append(ms.SQLcumQuert("lyproject", sqlstr));
        sqlstr = "select * from lyday where id in(select did from lyrt where jid=" + str(jid) + ")"
        print "sqlstr " + sqlstr
        vallist.append(ms.SQLcumQuert("lyday", sqlstr));
        sqlstr = "select * from lypoint where id in (select pid from lyrtp where did IN (select did from lyrt where jid=" + str(jid) + "))"
        print "sqlstr " + sqlstr
        vallist.append(ms.SQLcumQuert("lypoint", sqlstr));
    #插入point
        # did：天ID
        # ---vdct说明 vdct可以传任意字段 **必填
        # index:景点顺序  **
        # ptime:预计游玩时间
        # event：景点简介
        # name：景点名称 **
        # type：景点类型
        # transport：交通工具
        # trtime：交通用时
        # trevent：交通描述
        # picpath：图片路径预留
    def NewdDay(self, jid,vdct):
        cum = '';
        val = ''
        for key in vdct:
            cum = cum + key + ","
            val = val + "'" + vdct[key] + "',"
            print key + " " + vdct[key]
        cum = cum[:-1];
        val = val[:-1];
        ms = MySqlconc()
        sqlstr = "INSERT INTO lyday (" + cum + ") VALUES (" + val + ")"
        print "sqlstr " + sqlstr
        enum = ms.SQLexecute(sqlstr)
        sqls = "select max(id) from lyday"
        reid = ms.SQLQuery(sqls)
        maxdid = 0
        for idval in reid:
            for mid in idval:
                maxdid = mid
        print  maxdid
        sqlstr = "INSERT INTO lyrt (jid,did) VALUES ("+ str(jid)+","+str(maxdid)+")"
        print   sqlstr
        enum = ms.SQLexecute(sqlstr)
        return maxdid

    #修改day
        # did：天ID
        # ---vdct说明，vdct可以传任意字段
        # daynum:第几天
        # name:当天说明
        # 返回值：返回修改的影响的行数
    def EidtDay(self, did, vdct):
        setval = '';
        for key in vdct:
            setval = setval + key +"='"+vdct[key]+ "',"
        setval = setval[:-1];
        ms = MySqlconc()
        sqlstr = "UPDATE lyday SET "+setval+" where id="+str(did)
        print "sqlstr " + sqlstr
        enum = ms.SQLexecute(sqlstr)
        return enum

        # 删除day
        # did：天ID
        # 返回值：1 成功，0 失败
    def DelDay(self, did):
        ms = MySqlconc()
        sqlstr = "DELETE FROM lyday WHERE id in(select did from lyrt where did=" + str(did) + ")"
        print "sqlstr " + sqlstr
        enum2 = ms.SQLexecute(sqlstr)
        sqlstr = "DELETE FROM lypoint WHERE id in( select pid from lyrtp where did="+str(did)+") "
        print "sqlstr " + sqlstr
        enum3 = ms.SQLexecute(sqlstr)
        sqlstr = "DELETE FROM lyrtp WHERE did =did="+str(did)+") "
        print "sqlstr " + sqlstr
        enum4 = ms.SQLexecute(sqlstr)
        sqlstr = "DELETE FROM lyrt WHERE did="+str(did)+") "
        print "sqlstr " + sqlstr
        enum5 = ms.SQLexecute(sqlstr)
        return  enum2

    # 根据计划ID查询该计划下所有天数
    # jid：计划ID
    # 返回值：
    def QueryDayByJID(self, jid):
        ms = MySqlconc()
        sqlstr = "select * from lyday where id in(select did from lyrt where jid=" + str(jid) + ")"
        print "sqlstr " + sqlstr
        return ms.SQLcumQuert("lyproject", sqlstr)

    #插入point
        # did：天ID
        # ---vdct说明 vdct可以传任意字段 **必填
        # index:景点顺序  **
        # ptime:预计游玩时间
        # event：景点简介
        # name：景点名称 **
        # type：景点类型
        # transport：交通工具
        # trtime：交通用时
        # trevent：交通描述
        # picpath：图片路径预留
    # 返回值：新增point的ID
    def NewPoint(self, did,vdct):
        cum = '';
        val = ''
        for key in vdct:
            cum = cum + key + ","
            val = val + "'" + vdct[key] + "',"
            print key + " " + vdct[key]
        cum = cum[:-1];
        val = val[:-1];
        ms = MySqlconc()
        sqlstr = "INSERT INTO lypoint (" + cum + ") VALUES (" + val + ")"
        print "sqlstr " + sqlstr
        enum = ms.SQLexecute(sqlstr)
        sqls = "select max(id) from lypoint"
        reid = ms.SQLQuery(sqls)
        maxdid = 0
        for idval in reid:
            for mid in idval:
                maxdid = mid
        print  maxdid
        sqlstr = "INSERT INTO lyrtp (did,pid) VALUES ("+ str(did)+","+str(maxdid)+")"
        print   sqlstr
        enum = ms.SQLexecute(sqlstr)
        return maxdid

    #修改景点
        # pid：景点ID
        # ---vdct说明 vdct可以传任意字段 **必填
        # index:景点顺序  **
        # ptime:预计游玩时间
        # event：景点简介
        # name：景点名称 **
        # type：景点类型
        # transport：交通工具
        # trtime：交通用时
        # trevent：交通描述
        # picpath：图片路径预留
    # 返回值：返回修改的影响的行数
    def EidtPoint(self, pid, vdct):
        setval = '';
        for key in vdct:
            setval = setval + key +"='"+vdct[key]+ "',"
        setval = setval[:-1];
        ms = MySqlconc()
        sqlstr = "UPDATE lypoint SET "+setval+" where id="+str(pid)
        print "sqlstr " + sqlstr
        enum = ms.SQLexecute(sqlstr)
        return enum

        # 删除景点
        # 删除景点
        # pid：景点id
        # 返回值：1 成功，0 失败
    def DelPoint(self, pid):
        ms = MySqlconc()
        sqlstr = "DELETE FROM lypoint WHERE id=" + str(pid)
        print "sqlstr " + sqlstr
        enum1 = ms.SQLexecute(sqlstr)
        sqlstr = "DELETE FROM lyrtp WHERE pid=" + str(pid)
        print "sqlstr " + sqlstr
        enum2 = ms.SQLexecute(sqlstr)
        return  enum1
    # 根据天ID查询该计划下所有天数
    # did：天id
    # 返回值：
    def QueryPointByJID(self, did):
        ms = MySqlconc()
        sqlstr = "select * from lypoint where id in(select pid from lyrtp where did=" + str(did) + ")"
        print "sqlstr " + sqlstr
        return ms.SQLcumQuert("lyproject", sqlstr)
# 初始行政区数据
    def CreateXzq(self):
        jsonShen= urllib2.urlopen('https://route.showapi.com/268-2?showapi_appid=59865&showapi_test_draft=false&showapi_timestamp=20180420111616&showapi_sign=ece7531dc98a7584edff4751f6cfaf4a').read()
        python_to_json = json.loads(jsonShen)
        # print python_to_json
        # print type(python_to_json)
        listitem=python_to_json['showapi_res_body']
        print listitem
        if listitem.has_key('list'):
            items= listitem['list']
            ms = MySqlconc()
            print items
            for item in items:
               sqlstr=  "INSERT INTO xzqinfo (id,name,pid) VALUES ("+item['id']+",'"+item['name']+"',0)"
               enum = ms.SQLexecute(sqlstr)
               self.CreateXzqCity(item['id'])
               print item

    # 初始行政区数据
    def CreateXzqCity(self,id):
        url="https://route.showapi.com/268-3?proId="+id+"&showapi_appid=59865&showapi_test_draft=false&showapi_timestamp=20180420111649&showapi_sign=1c0eda05ab15436d8c6b5c9dbe1e023c"
        print url
        time.sleep(1)
        jsonShen = urllib2.urlopen(url).read()
        python_to_json = json.loads(jsonShen)
        print python_to_json
        # print type(python_to_json)
        listitem = python_to_json['showapi_res_body']
        print listitem
        if listitem.has_key('list'):
            items = listitem['list']
            ms = MySqlconc()
            print items
            nowcityid=""
            for item in items:
                # if item.has_key('cityId'):
                #     sqlstr = "INSERT INTO xzqinfo (id,name,pid) VALUES (" + item['cityId'] + ",'" + item[
                #         'proName'] + "'," + id + ")"
                if item.has_key('cityId'):
                    if nowcityid!= item['cityId']:
                        print nowcityid+" "+ item['cityId']
                        sqlstr = "INSERT INTO xzqinfo (id,name,pid) VALUES (" + item['cityId'] + ",'" + item[
                            'cityName'] + "'," + id + ")"
                        enum = ms.SQLexecute(sqlstr)
                        nowcityid= item['cityId']
            print item

        # for (k, v) in python_to_json.items():
        #     print  str(k)+"    "+str(v)
