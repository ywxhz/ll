#!/usr/bin/env pytho
# -- coding: UTF-8
from MySqlCon import MySqlconc
import json
import urllib2
import time


class DataServicec:
    fslyday = []
    fslypoint = []
    fslyproject = []
    def getlydayfs(self,filed):
        fs=[]
        if len(self.fslyday) == 0:
            ms = MySqlconc()
            sqlstr = "select COLUMN_NAME from information_schema.columns where table_name='lyday'"
            self.fslyday = ms.SQLQuery(sqlstr)
        fs = self.fslyday
        hf=False
        for f in fs:
            vl=str(f)[3:-3]
            if  filed ==vl:
                hf=True
        return hf
    def getlypointfs(self,filed):
        fs=[]
        if len(self.fslypoint)==0:
            ms = MySqlconc()
            sqlstr = "select COLUMN_NAME from information_schema.columns where table_name='lypoint'"
            self.fslypoint=ms.SQLQuery(sqlstr)
        fs = self.fslypoint
        hf=False
        for f in fs:
            vl=str(f)[3:-3]
            if  filed ==vl:
                hf=True
        return hf
    def getlyprojectfs(self,filed):
        fs=[]
        if len(self.fslyproject) == 0:
            ms = MySqlconc()
            sqlstr = "select COLUMN_NAME from information_schema.columns where table_name='lyproject'"
            self.fslyproject = ms.SQLQuery(sqlstr)
        fs = self.fslyproject
        hf=False
        for f in fs:
            vl=str(f)[3:-3]
            # print filed +" "+vl
            if  filed ==vl:
                hf=True
        return hf

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
        cum=''
        val=''
        for key in vdct:
            if self.getlyprojectfs(key):
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

    def Queryxzq(self):
        # Fstr = '';
        # for key in vdct:
        #     Fstr = Fstr + key +" like '%"+vdct[key]+"%' or"
        #     print Fstr
        # Fstr = Fstr[:-2];
        ms = MySqlconc()
        sqlstr = "select * from xzqinfo ORDER BY szm"
        print "sqlstr " + sqlstr
        return ms.SQLcumQuert('xzqinfo',sqlstr)

        # 插入day
        # jid：计划ID
        # ---vdct说明 vdct可以传任意字段
        # daynum:第几天
        # name:当天说明
        # 返回值：新增天的ID
    # 修改project
    # jid：计划ID
    # ---vdct说明，vdct可以传任意字段
    # name:计划名称
    # event:计划描述
    # 返回值：返回修改的影响的行数
    def EidtProject(self, jid, vdct):
        setval = '';
        for key in vdct:
            if self.getlyprojectfs(key):
                setval = setval + key + "='" + vdct[key] + "',"
        setval = setval[:-1];
        ms = MySqlconc()
        sqlstr = "UPDATE lyproject SET " + setval + " where id=" + str(jid)
        print "sqlstr " + sqlstr
        enum = ms.SQLexecute(sqlstr)
        msg = ""
        msgval = -1
        if enum == 0:
            msg = ms.getsqlmsg()
        else:
            msg = "修改成功"
            msgval = jid
        dict = {}
        dict['msg'] = msg
        dict['val'] = msgval
        print str(dict)
        return dict

    def EidtProjectEnum(self, jid, vdct):
        setval = '';
        for key in vdct:
            if self.getlyprojectfs(key):
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
        sqlstr = "select * from lyproject where name like '%"+qv+"%' or event like '%"+qv+"%' or price like '%"+qv+"%' ORDER BY id DESC limit 20 "
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
        vallist = {}
        ms = MySqlconc()
        sqlstr = "select * from lyproject where id =" + str(jid)+" ORDER BY id DESC"
        print "sqlstr " + sqlstr
        vallist['lyproject']=ms.SQLcumQuert("lyproject", sqlstr)
        sqlstr = "select * from lyday where id in(select did from lyrt where jid=" + str(jid) + ") ORDER BY daynum"
        print "sqlstr " + sqlstr
        vallist['lyday'] =ms.SQLcumQuert("lyday", sqlstr)
        sqlstr = "select lyrt.jid,lyrtp.did,lypoint.* from lyrtp,lyrt,lypoint where lyrtp.did=lyrt.did and lyrtp.pid=lypoint.id and lyrt.jid=" + str(jid)+" ORDER BY lypoint.indexnum  "
        print "sqlstr " + sqlstr
        vallist['lypoint'] =ms.SQLcumQuert1("lypoint", sqlstr, ['jid', 'did'])
        # print vallist
        return vallist

    def QueryInfoByJIDdesc(self, jid):
        vallist = {}
        ms = MySqlconc()
        sqlstr = "select * from lyproject where id =" + str(jid) + " ORDER BY id "
        print "sqlstr " + sqlstr
        vallist['lyproject'] = ms.SQLcumQuert("lyproject", sqlstr)
        sqlstr = "select * from lyday where id in(select did from lyrt where jid=" + str(jid) + ") ORDER BY daynum"
        print "sqlstr " + sqlstr
        vallist['lyday'] = ms.SQLcumQuert("lyday", sqlstr)
        sqlstr = "select lyrt.jid,lyrtp.did,lypoint.* from lyrtp,lyrt,lypoint where lyrtp.did=lyrt.did and lyrtp.pid=lypoint.id and lyrt.jid=" + str(jid) + " ORDER BY lypoint.indexnum "
        print "sqlstr " + sqlstr
        vallist['lypoint'] = ms.SQLcumQuert1("lypoint", sqlstr, ['jid', 'did'])
        # print vallist
        return vallist
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
        cum = ''
        val = ''
        ms = MySqlconc()
        # 获取最大index
        sqls = "select max(daynum) from lyday WHERE id IN (select did from lyrt WHERE jid=" + jid + ")"
        reid = ms.SQLQuery(sqls)
        maxindex = 0
        for idval in reid:
            for mid in idval:
                if not mid is None:
                    maxindex = mid
        print  maxindex
        # 获取最大index
        vdct = vdct.to_dict()
        print type(vdct)
        vdct['daynum'] = maxindex + 100
        for key in vdct:
            if self.getlydayfs(key):
                if key == "daynum":
                    cum = cum + key + ","
                    val = val + str(vdct[key]) + ","
                else:
                    cum = cum + key + ","
                    val = val + "'" + vdct[key] + "',"
                    # print key + " " + vdct[key]
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
        setval = ''
        for key in vdct:
            if self.getlydayfs(key):
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
        sqlstr = "DELETE FROM lyrtp WHERE did ="+str(did)+") "
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
        cum = ''
        val = ''
        ms = MySqlconc()
        # 获取最大index
        sqls = "select max(indexnum) from lypoint WHERE id IN (select pid from lyrtp WHERE did=" + did + ")"
        reid = ms.SQLQuery(sqls)
        maxindex = 0
        for idval in reid:
            for mid in idval:
                if not mid is None:
                    maxindex = mid
        print  maxindex
        # 获取最大index
        vdct=vdct.to_dict()
        print type(vdct)
        vdct['indexnum']=maxindex+100
        for key in vdct:
            if self.getlypointfs(key):
                if key=="indexnum":
                    cum = cum + key + ","
                    val = val + str(vdct[key]) + ","
                else:
                    cum = cum + key + ","
                    val = val + "'" + vdct[key] + "',"
                # print key + " " + vdct[key]
        cum = cum[:-1]
        val = val[:-1]
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
        print  sqlstr
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
        setval = ''
        for key in vdct:
            if self.getlypointfs(key):
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
            # print items
            for item in items:
               sqlstr=  "INSERT INTO xzqinfo (id,name,pid) VALUES ("+item['id']+",'"+item['name']+"',0)"
               enum = ms.SQLexecute(sqlstr)
               self.CreateXzqCity(item['id'])
               # print item

    # 初始行政区数据
    def CreateXzqCity(self,id):
        url="https://route.showapi.com/268-3?proId="+id+"&showapi_appid=59865&showapi_test_draft=false&showapi_timestamp=20180424110843&showapi_sign=1c0eda05ab15436d8c6b5c9dbe1e023c"
        print url
        time.sleep(1)
        jsonShen = urllib2.urlopen(url).read()
        python_to_json = json.loads(jsonShen)
        # print python_to_json
        # print type(python_to_json)
        listitem = python_to_json['showapi_res_body']
        # print listitem
        if listitem.has_key('list'):
            items = listitem['list']
            ms = MySqlconc()
            # print items
            nowcityid=""
            for item in items:
                # if item.has_key('cityId'):
                #     sqlstr = "INSERT INTO xzqinfo (id,name,pid) VALUES (" + item['cityId'] + ",'" + item[
                #         'proName'] + "'," + id + ")"
                if item.has_key('cityId'):
                    if nowcityid!= item['cityId']:
                        # print nowcityid+" "+ item['cityId']
                        sqlstr = "INSERT INTO xzqinfo (id,name,pid) VALUES (" + item['cityId'] + ",'" + item[
                            'cityName'] + "'," + id + ")"
                        enum = ms.SQLexecute(sqlstr)
                        nowcityid= item['cityId']
            # print item
    # 复制数据
    # 输入要复制的projectid
    # newname新的名称
    def copyDataByPid(self,id,vdct):
        ms = MySqlconc()
        #插入新project行
        sqls = "insert into lyproject(day,event,keywords,picpath,price) select day,event,keywords,picpath,price from lyproject where id="+str(id)
        reid = ms.SQLexecute(sqls)
        # 获取最大jid---{
        sqls = "select max(id) from lyproject"
        reidQ = ms.SQLQuery(sqls)
        maxjid = 0
        for idval in reidQ:
            for mid in idval:
                maxjid = mid
        # 获取最大jid--}
        # sqlstr = "UPDATE lyproject SET name='"+newname+"' where id ="+str(maxjid)
        # #  返回值------------------
        # enumR = ms.SQLexecute(sqlstr)
        enumR=self.EidtProjectEnum(maxjid,vdct)
        msgval = -1
        dict = {}
        if enumR == 0:
            sqlstr = "DELETE FROM lyproject WHERE id=" + str(maxjid)
            ms.SQLexecute(sqlstr)
            dict['msg'] = ms.getsqlmsg()
            dict['msg'] = ms.getsqlmsg()
            dict['val'] = msgval
            print str(dict)
            return dict
        else:
            msgval = maxjid
            dict['msg'] = '成功'
            dict['val'] = msgval
        sqls = "select lyrt.did from lyrt,lyday WHERE lyday.id=lyrt.did AND lyrt.jid="+str(id)
        reidQ = ms.SQLQuery(sqls)
        print reidQ
        for idval in reidQ:
            print idval
            for did in idval:
                sqls = "insert into lyday(daynum,dayevent,name,picpath) select daynum,dayevent,name,picpath from lyday where id=" + str(did)
                reid = ms.SQLexecute(sqls)
                #  j d 插入关系表--
                sqls = "insert into lyrt(lyrt.jid,lyrt.did) select max(lyproject.id),max(lyday.id) from lyday,lyproject"
                reid = ms.SQLexecute(sqls)
                #循环插入point--
                sqls = "select lyrtp.pid from lyrtp,lypoint WHERE  lypoint.id=lyrtp.pid AND did=" + str(did)
                reidQ2 = ms.SQLQuery(sqls)
                print reidQ2
                for idval2 in reidQ2:
                    print idval2
                    for pid in idval2:
                        sqls = "insert into lypoint(indexnum,ptime,event,name,type,transport,trtime,treventds,picpath,stratt,stratc,stratp,endc,endt,endp,tptrain,tptrainevent,tptrainsp,trdistance) select indexnum,ptime,event,name,type,transport,trtime,treventds,picpath,stratt,stratc,stratp,endc,endt,endp,tptrain,tptrainevent,tptrainsp,trdistance from lypoint where id=" + str(pid)
                        reid = ms.SQLexecute(sqls)
                        #  dp 插入关系表--
                        sqls = "insert into lyrtp(did,pid) select max(lyday.id),max(lypoint.id) from lyday,lypoint"
                        reid = ms.SQLexecute(sqls)
        print str(dict)
        return dict
        # for (k, v) in python_to_json.items():
        #     print  str(k)+"    "+str(v)
