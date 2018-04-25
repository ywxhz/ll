# -- coding: UTF-8
from DataService import DataServicec

#print 1
ds = DataServicec();
#print 2
#ds.helloworld()
# dict={'name': '北京71133天', 'event': '北京故宫非常好玩，颐和园，长城等地方'}
# ds.NewProject(dict)
# dict={'name': '北京7222天', 'event': '北京故宫非常好玩111，颐和园222，长城等地方222'}
# ds.NewProject(dict)
# dict={'name': '北京7333天', 'event': '北京故宫非常好玩111，颐和园333，长城等地方333'}
# ds.EidtProject(31,dict)

# dict={'daynum': '10', 'name': '北京111长城'}
# ds.NewdDay(32,dict)
# dict={'daynum': '10', 'name': '北京故宫'}
# ds.EidtDay(8,dict)
# dict={'daynum': '10', 'name': '北京故宫'}
print ds.copyDataByPid(190,"南昌复制11")
# print ds.CreateXzqCity('14')
# print ds.getlydayfs('name')
# print ds.getlypointfs('event')
# print ds.getlyprojectfs('id')
# print ds.getlyprojectfs('xx')
# print ds.getlypointfs('xx')
# print ds.getlydayfs('123')
# print  ds.QueryProject("2")