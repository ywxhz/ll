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

