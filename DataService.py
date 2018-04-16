# -- coding: UTF-8
from MySqlCon import MySqlconc


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
        sqls="select max(id) from lyproject"
        reid=ms.SQLQuery(sqls)
        maxid=0
        for idval in reid:
            for mid in idval:
                maxid= mid
        print  maxid
        return maxid

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
        if enum1 > 0 and enum4 > 0 and enum5 > 0:
            return 1
        else:
            return 0
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
        sqlstr = "DELETE FROM lyday WHERE id in(select did from lyrt where id=" + str(did) + ")"
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
        if  enum4 > 0 and enum5 > 0:
            return 1
        else:
            return 0

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
        # pid：景点id
        # 返回值：1 成功，0 失败
    def DelDay(self, pid):
        ms = MySqlconc()
        sqlstr = "DELETE FROM lypoint WHERE id=" + str(pid)
        print "sqlstr " + sqlstr
        enum1 = ms.SQLexecute(sqlstr)
        sqlstr = "DELETE FROM lyrtp WHERE pid=" + str(pid)
        print "sqlstr " + sqlstr
        enum2 = ms.SQLexecute(sqlstr)
        if enum1>0 and enum2>0:
            return 1
        else:
            return 0



    # 根据天ID查询该计划下所有天数
    # did：天id
    # 返回值：
    def QueryPointByJID(self, did):
        ms = MySqlconc()
        sqlstr = "select * from lypoint where id in(select pid from lyrtp where did=" + str(did) + ")"
        print "sqlstr " + sqlstr
        return ms.SQLcumQuert("lyproject", sqlstr)
