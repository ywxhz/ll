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

    #插入day
        # jid：计划ID
        # ---vdct说明
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
        # pid：计划ID
        # vdct说明
        # name:计划名称
        # event:计划描述
        # 返回值：新增计划的ID
        def EidtDay(self, pid, vdct):
            return 0
    #插入景点


