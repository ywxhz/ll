#!/usr/bin/env pytho
# -- coding: UTF-8

import pymysql

class MySqlconc:
    conn = pymysql.connect(host='192.168.3.254', port=3306, user='lywz', passwd='123456', db='lydata', charset='utf8')
    def SQLexecute(self,sqlstr):
        # 创建连接
        effect_row=0
        # 创建游标
        cursor = self.conn.cursor()
        # 执行SQL，并返回收影响行数
        effect_row = cursor.execute(sqlstr)
        # 执行SQL，并返回受影响行数
        # effect_row = cursor.execute("update tb7 set pass = '123' where nid = %s", (11,))
        # 执行SQL，并返回受影响行数,执行多次
        # effect_row = cursor.executemany("insert into tb7(user,pass,licnese)values(%s,%s,%s)", [("u1","u1pass","11111"),("u2","u2pass","22222")])
        # 提交，不然无法保存新建或者修改的数据
        self.conn.commit()
        # 关闭游标
        cursor.close()
        # 关闭连接
        self.conn.close()
        return effect_row

    def SQLQuert(self,sqlstr):
        # ! /usr/bin/env python
        # -*- coding:utf-8 -*-
        # __author__ = "TKQ"
        import pymysql
        cursor = self.conn.cursor()
        cursor.execute(sqlstr)
        result = cursor.fetchall()

        # for i in result:
        #     print i
        #     for j in i:
        #         print j
        # 获取剩余结果的第一行数据
        #row_1 = cursor.fetchone()
        #print row_1
        # 获取剩余结果前n行数据
        #row_2 = cursor.fetchmany(3)
        #print row_2
        # 获取剩余结果所有数据
        # row_3 = cursor.fetchall()
        self.conn.commit()
        cursor.close()
        self.conn.close()
        return  result

    def SQLcumQuert(self,tbName,sqlstr):
        tbcom="select COLUMN_NAME from information_schema.columns where table_name='" + tbName+"'"
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
        for i in valresult:
            dict = {}
            cnum = 0
            for j in i:
                dict["'"+cumlist[cnum]+"'"]= j
            dictlist.append(dict)
        print dictlist
        self.conn.commit()
        valcursor.close()
        cumcursor.close()
        self.conn.close()
        return  dictlist

