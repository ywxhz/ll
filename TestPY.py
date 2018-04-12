# -- coding: UTF-8
from DataService import DataServicec

#print 1
ds = DataServicec();
#print 2
#ds.helloworld()
#dict={'name': '北京7天', 'event': '北京故宫非常好玩，颐和园，长城等地方'}
#ds.NewProject(dict)
dict={'daynum': '7', 'name': '北京长城'}
ds.NewdDay(30,dict)