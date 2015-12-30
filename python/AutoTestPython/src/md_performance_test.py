# coding=gbk
'''
Created on 2011-8-7

@author: Administrator
'''
import win32com.client
import traceback
from navapp import autotest
from navapp import navitool
from testcase.md import test_display_performance
import time
import fixture
import os
import shutil

TestName = 'MD性能测试'
localt = time.localtime()
TestTime = '%04d-%02d-%02d-%02d-%02d-%02d'%(localt[0],localt[1],localt[2],localt[3],localt[4],localt[5])

fixture.connectdevice()

excel = win32com.client.Dispatch("Excel.Application")
excel.DisplayAlerts = False
filename = (fixture.SourceDir + 'MD_性能测试2.xlsx').decode('gbk')
output = (fixture.OutDir + '基础数据应用层测试检查list_output.xls').decode('gbk')
d1 = excel.Workbooks.Open(Filename = filename)
sheet = d1.Sheets('MD性能测试')

perf_base = int(sheet.Range('C3').Text)
scalemap = {'50m':17,'100m':16,'200m':15,'400m':14,'800m':13,'1km':12,'2km':11,'4km':10,'10km':9,'20km':8,'40km':7}
cols = ['D','E','F','G','H','I','J']
for line in range(6,32):
    if len(sheet.Range('A%d'%line).Text)>0:city = sheet.Range('A%d'%line).Text
    if len(sheet.Range('B%d'%line).Text)>0:rect = sheet.Range('B%d'%line).Text
    o = sheet.Range('C%d'%line)
    if(len(o.Text)!=0):
        print('Rendering... ' + city + ':' + o.Text)
        try:
            testok,rlst = test_display_performance.dotest(georect=rect.encode('utf-8'),base = perf_base,scaleindex=scalemap[o.Text.encode('utf-8')])
        except:
            print '测试出现崩溃'
            teskok = False
            sheet.Rows('%d:%d'%(line,line)).Interior.ColorIndex = 3
            sheet.Rows('%d:%d'%(line,line)).Interior.Pattern = 1
            continue
        #填充Excel
        for i in range(0,5):
            col = (cols[i]+"%d")%line
            sheet.Range(col).FormulaR1C1 = rlst[i]
        col = (cols[6]+"%d")%line
        logName = (os.path.join(fixture.OutDir,'md_perf.log')).decode('gbk')
        try:
            pic = sheet.OLEObjects().Add(Filename=logName, Link=False, DisplayAsIcon=False)
            pic.ShapeRange.Height = 20
            pic.ShapeRange.Width = 20
            pic.ShapeRange.Left = sheet.Range(col).Left
            pic.ShapeRange.Top = sheet.Range(col).Top
        except:
            None
        cell = sheet.Range((cols[5]+"%d")%line)
        cell.AddComment()
        cell.Comment.Visible = False
        cell.Comment.Shape.Fill.UserPicture(os.path.join(fixture.OutDir,'md_heatmap.png'))
        cell.Comment.Shape.Fill.Visible = True
        cell.Comment.Shape.Width = 480
        cell.Comment.Shape.Height = 272
        #建立目录备份测试结果
        TestCaseNo = city + '_' + o.Text
        BackupDir = os.path.join(fixture.OutDir,TestName,TestTime,TestCaseNo)
        os.makedirs(BackupDir)
        for p in os.listdir(fixture.OutDir):
            f = os.path.join( fixture.OutDir, p )
            if os.path.isfile( f ):
                shutil.copyfile(f,os.path.join(BackupDir,p))
        

fixture.closedevice()

for i in xrange(d1.Sheets.Count,0,-1):
    if d1.Sheets(i) != sheet:
        d1.Sheets(i).Delete()
d1.SaveAs(output)
d1.Close()
excel = None

#输出Excel：
backdir = os.path.join(fixture.OutDir , TestName, TestTime)
try:
    os.makedirs(backdir)
except: 
    None
shutil.copyfile(output,os.path.join(backdir , '基础数据应用层测试检查list_output.xls'))


