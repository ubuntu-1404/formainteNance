# coding=gbk
'''
Created on 2011-8-25

@author: Administrator
'''
import fixture
from fixture import utility
from navapp import navitool
from navapp import autotest
import time
import re

def dotest(*args,**kwargs):
    fixture.setup()
    #默认搜索类型为POI
    find_type = 'poi'
    if (kwargs.has_key('find_type')):
        find_type = kwargs['find_type']
        if find_type == '名称搜索':
            find_type = 'poi'
        elif find_type == '门址搜索':
            find_type = 'address'
        elif find_type == '交叉路口':
            find_type = 'cross'
        else:
            find_type = ''
        
    #默认搜索区域为北京
    districtccode = 110000
    if (kwargs.has_key('districtccode')):
        if len(re.findall('\d+,\d+',kwargs['districtccode'])) == 1:
            t = re.split(',',kwargs['districtccode'])
        else:
            districtccode = int(kwargs['districtccode'][0:6])
        
    #输入名称
    input_name = ''
    if (kwargs.has_key('input_name')):
        input_name = kwargs['input_name']   
    #输入方式
    input_type = ''
    if (kwargs.has_key('input_type')):
        input_type = kwargs['input_type'] 
    
    #print(len(navitool.find_py('poi', 100000, 'yjjj')))
    if input_type == '关键字':
        result = len(navitool.find_keyword(find_type, districtccode, input_name))
    elif input_type == '拼音':
        result = len(navitool.find_py(find_type, districtccode, input_name))
    else:
        input_name1 = input_name.split(',')
        result = len(navitool.find_around(input_name1, int(t[0]), int(t[1])))
    fixture.teardown()
    return result

if __name__=='__main__':
    #testok = navitool.find_around('0X4100001,0X10200025,0X10100024', 11629271, 4004616)
    #testok = dotest(find_type='poi',districtccode ='1100000', input_name ='上岛咖啡',input_type='关键字')
    testok = dotest(find_type='',districtccode ='11629271,4004616', input_name='0X4100001,0X10200025,0X10100024',input_type='')
    print(testok)
    