# coding=gbk
'''
Created on 2011-8-5

@author: Administrator
'''
import re
from navapp import xxtool

def trans_startend(str):
    g = re.split('[ ,] *',str)
    return {'lon':int(g[0]),'lat':int(g[1])},{'lon':int(g[2]),'lat':int(g[3])}

def trans_pointlst(str):
    g = re.split('[ ,] *',str)
    mid = []
    for i in range(0,len(g)/2):
        mid.append({'lon':int(g[i*2]),'lat':int(g[i*2+1])})
    return mid

def decode_coor(c):
    s = re.sub('-','',c)
    return xxtool.DecodeCoor(s)

def trans_decodecoor(str):
    g = re.findall('\d\d\d\d\-\d\d\d\d\-\d\d\d\d',str)
    if len(g) == 0:return str
    for i in g:
        if(len(i)!=14):  raise 'Format Error!'
    lst = ''
    for n in range(0,len(g)):
        lst = lst + decode_coor(g[n]) + ','
    return lst
    
def compare_time(t1,t2):
    t01 = re.split(':',t1)
    t02 = re.split(':',t2)
    if(int(t01[0]) < int(t02[0])):
        return -1    
    if(int(t01[0]) > int(t02[0])):
        return 1
    if(int(t01[1]) < int(t02[1])):
        return -1    
    if(int(t01[1]) > int(t02[1])):
        return 1
    if(int(t01[2]) < int(t02[2])):
        return -1    
    if(int(t01[2]) > int(t02[2])):
        return 1
    return 0
            