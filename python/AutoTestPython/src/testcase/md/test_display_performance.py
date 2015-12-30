# coding=gbk
'''
Created on 2011-8-23

@author: Administrator
'''
import fixture
from fixture import utility
from fixture import colorschemes
from navapp import navitool
from navapp import autotest
import time
import os
import Image
import ImageDraw

def dotest(*args, **kwargs):
    fixture.setup()
    pt = utility.trans_pointlst(kwargs['georect'])
    index = kwargs['scaleindex']
    base = kwargs['base']
    
    navitool.map_zoomscaleindex(index)
    navitool.map_setcenter(pt[0]['lon'],pt[0]['lat'])#�ӱ����ϻ��Ʊ���ī����ЧӦ
    w,h = navitool.map_currgeosizeofscreen()
    rlst = [(x,y) for y in xrange(pt[1]['lat'],pt[0]['lat']+h,h) for x in xrange(pt[0]['lon'],pt[1]['lon']+w,w)]
    maxtime = 0
    result = []
    sum = 0
    try:
        
        for r in rlst:
            navitool.map_setcenter(r[0],r[1])
            t0 = autotest.md_performance()
            t1 = autotest.md_performance()
            rtime = (t0+t1)/2
            if rtime > base * 3 or abs(t1-t0) > base:
                time.sleep(1)
                rtime = (autotest.md_performance()+autotest.md_performance())/2
            if rtime > maxtime:maxtime = rtime
            result.append((r[0],r[1],rtime))
            sum = sum + rtime
    except:
            print r
            raise

    
    result.sort(lambda x,y:y[2]-x[2])#����Ⱦ�ٶ������������򣬲�����log
    fp = open(os.path.join(fixture.OutDir,"md_perf.log"),"w")
    for t in result: fp.write("%d,%d,%d\n"%t)
    fp.close()
    countBase2 = len([t for t in result if t[2] > base*2])#��Ⱦʱ�䳬��base*2�Ĵ���
    countBase = len([t for t in result if t[2] > base])#��Ⱦʱ�䳬��base�Ĵ���
    av_time = float(sum)/len(result)
    #��ͼ��Ϊ�ȶ�ͼ����ͼ
    navitool.map_zoomrect(pt[0]['lon'], pt[1]['lat'], pt[1]['lon'], pt[0]['lat'])
    autotest.md_performance()#Ҫ����һ��
    autotest.screen_snapshot('heatbase.png')
    #�ȶ�ӳ��
    mapcolor = lambda time:min(max(255-110*(time - base)/(2*base-base) - 90,10),230)
        
    #����ȶ�ͼ
    im = Image.new('RGB',navitool.map_screensize())
    draw = ImageDraw.Draw( im )
    for t in result:
        p0 = navitool.map_lp2dp(t[0]-w/2, t[1]+h/2)
        p1 = navitool.map_lp2dp(t[0]+w/2, t[1]-h/2)
        draw.rectangle(p0+p1,fill=colorschemes.schemes['classic'][mapcolor(t[2])])
    fixture.teardown()
    snap_im = Image.open(os.path.join(fixture.OutDir,"heatbase.png"))
    if im.size != snap_im.size:im = im.resize(snap_im.size)
    im = Image.blend(snap_im,im,0.75)
    im.save(os.path.join(fixture.OutDir,'md_heatmap.png'),'PNG')
    return True,(len(result)-countBase,countBase-countBase2,countBase2,av_time,maxtime)
    
if __name__ == "__main__":
    testok,result = dotest(georect='11625038,4000870 11653713,3982608',scaleindex=15,base=20)
    