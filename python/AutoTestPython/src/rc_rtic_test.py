# coding=gbk
'''
Created on 2011-8-7

@author: Administrator
'''
import win32com.client
import traceback
from navapp import autotest
from navapp import navitool
from testcase.rc import test_calc_rtic
import time
import fixture
import re
import os
import shutil

TestName = 'RTIC合理性测试'
localt = time.localtime()
TestTime = '%04d-%02d-%02d-%02d-%02d-%02d'%(localt[0],localt[1],localt[2],localt[3],localt[4],localt[5])
RticSrcDir = 'c:\\TestSource\\rtic\\shanghai\\' 
#RticDstDir = 'C:\\Users\\lichen\\MyWork\\source\\pc\\cyx3.5\\cmmbdata\\mot\\tti\\'
RticDstDir = '\\residentflash\\CMMBDATA\\MOT\\tti\\'
fixture.connectdevice()

excel = win32com.client.Dispatch("Excel.Application")
excel.DisplayAlerts = False
filename = (fixture.SourceDir + 'its_rtic用例.xlsx').decode('gbk')
output = (fixture.OutDir + '基础数据应用层测试检查list_output.xls').decode('gbk')
d1 = excel.Workbooks.Open(Filename = filename)
sheet = d1.Sheets('路线整理')
scalemap = {'20m':18,'50m':17,'100m':16,'200m':15,'400m':14,'800m':13,'1km':12,'2km':11,'4km':10,'10km':9,'20km':8,'40km':7}

for line in range(84,88):
    o = sheet.Range('B%d'%line)
    rtictime = (sheet.Range('C%d'%line).Text).encode('gbk')
    zoompoint = sheet.Range('F%d'%line).Text.encode('utf-8')
    zoomindex = sheet.Range('G%d'%line).Text.encode('utf-8')
    if zoompoint == '':zoompoint = None
    scalei = None
    if zoomindex == '':
        zoomindex = None
    else:
        scalei=scalemap[zoomindex]
    if(len(o.Text)!=0):
        print('Calculating... ' + o.Text)
        try:
            testok,rlst = test_calc_rtic.dotest(start_end=o.Text.encode('utf-8'),bugpoint=zoompoint,scaleindex=scalei,caseno=rtictime,casesrcdir=RticSrcDir,casedstdir=RticDstDir)
        except:
            print '测试出现崩溃'
            teskok = False
            #把整行标为红色
            sheet.Rows('%d:%d'%(line,line)).Interior.ColorIndex = 3
            sheet.Rows('%d:%d'%(line,line)).Interior.Pattern = 1
            continue
        print(rlst)
        #填充Excel
        for i in range(0,1):
            #插入截图到excel中
            cell = sheet.Range(("E%d")%line)
            if cell.Comment==None:cell.AddComment()
            cell.Comment.Visible = False
            cell.Comment.Shape.Fill.UserPicture(os.path.join(fixture.OutDir,'route0.png'))
            cell.Comment.Shape.Fill.Visible = True
            cell.Comment.Shape.Width = 480
            cell.Comment.Shape.Height = 272
            if zoompoint != None:
                #插入截图到excel中
                cell = sheet.Range(("F%d")%line)
                if cell.Comment==None:cell.AddComment()
                cell.Comment.Visible = False
                cell.Comment.Shape.Fill.UserPicture(os.path.join(fixture.OutDir,'route00.png'))
                cell.Comment.Shape.Fill.Visible = True
                cell.Comment.Shape.Width = 480
                cell.Comment.Shape.Height = 272
        #建立目录备份测试结果
        TestCaseNo = str(line)
        BackupDir = os.path.join(fixture.OutDir,TestName,TestTime,TestCaseNo)
        os.makedirs(BackupDir)
        for p in os.listdir(fixture.OutDir):
            f = os.path.join( fixture.OutDir, p )
            if os.path.isfile( f ):
                shutil.copyfile(f,os.path.join(BackupDir,p))
    else:break

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
shutil.copyfile(output,os.path.join(backdir , '基础数据应用层测试检查list_RC.xls'))

