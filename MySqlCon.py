#!/usr/bin/env pytho
# -- coding: UTF-8

import pymysql

class MySqlconc:
    conn = pymysql.connect(host='192.168.3.254', port=3306, user='lywz', passwd='123456', db='lydata',charset='utf8')
    sqlmsg="错误"
    def Connopen(self):
        return 0
    def getsqlmsg(self):
        return self.sqlmsg
    def SQLexecute(self,sqlstr):
        self.conn = pymysql.connect(host='192.168.3.254', port=3306, user='lywz', passwd='123456', db='lydata',charset='utf8')
        # 创建连接
        effect_row=0
        # 创建游标
        cursor =self.conn.cursor()
        try:
            effect_row = cursor.execute(sqlstr)
            self.conn.commit()
        except Exception as e:
            print (str(e))
            if e[0]==1062:
                self.sqlmsg="IIException:mysql code:1062,The field unique value has already existed 唯一值存在"
            return effect_row
        # 执行SQL，并返回收影响行数

        # 关闭游标
        cursor.close()
        # 关闭连接
        self.conn.close()
        return effect_row

    def SQLQuery(self,sqlstr):
        self.conn = pymysql.connect(host='192.168.3.254', port=3306, user='lywz', passwd='123456', db='lydata',charset='utf8')
        print sqlstr
        cursor = self.conn.cursor()
        cursor.execute(sqlstr)
        result = cursor.fetchall()
        self.conn.close()
        return  result

    def SQLcumQuert(self,tbName,sqlstr):
        self.conn = pymysql.connect(host='192.168.3.254', port=3306, user='lywz', passwd='123456', db='lydata',charset='utf8')
        print tbName+" "+sqlstr
        tbcom="select COLUMN_NAME from information_schema.columns where table_name='" + tbName+"'"
        print tbcom
        cumcursor = self.conn.cursor()
        valcursor= self.conn.cursor()
        cumcursor.execute(tbcom)
        valcursor.execute(sqlstr)
        cumresult = cumcursor.fetchall()
        valresult = valcursor.fetchall()
        cumlist = []
        for rowval in cumresult:
            #print i
            for cumval in rowval:
                cumlist.append(cumval)
                #print cumlist
        dictlist=[]
        for valr in valresult:
            dict = {}
            cnum = 0
            #print valr
            for va in valr:
                dict[cumlist[cnum]]= va
                cnum = cnum + 1
                #print va
            dictlist.append(dict)

        self.conn.commit()
        valcursor.close()
        cumcursor.close()
        self.conn.close()
        return  dictlist

