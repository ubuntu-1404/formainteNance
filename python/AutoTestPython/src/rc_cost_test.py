# coding=gbk
'''
Created on 2011-8-7

@author: Administrator
'''
import win32com.client
import traceback
from navapp import autotest
from navapp import navitool
from testcase.rc import test_calc_mincost
import time
import fixture
import re
import os
import shutil

TestName = 'RC合理性测试'
localt = time.localtime()
TestTime = '%04d-%02d-%02d-%02d-%02d-%02d'%(localt[0],localt[1],localt[2],localt[3],localt[4],localt[5])

excel = win32com.client.Dispatch("Excel.Application")
excel.DisplayAlerts = False
filename = (fixture.SourceDir + '基础数据应用层测试检查list.xls').decode('gbk')
output = (fixture.OutDir + '基础数据应用层测试检查list_output.xls').decode('gbk')
d1 = excel.Workbooks.Open(Filename = filename)
sheet = d1.Sheets('RC用例库')
#填充距离/时间数据列
cols = ['G','H','I','J']
#截图数据列
cols2= ['U','V','W','X']

for c in cols2:#为了截图调整列宽
    sheet.Columns(c + ':' + c).ColumnWidth = 24
for line in range(4,484):
    o = sheet.Range('E%d'%line)
    ref = sheet.Range('F%d'%line)
    if(len(o.Text)!=0):
        print('Calculating... ' + o.Text)
        reflst = ref.Text.encode('utf-8')
        try:
            testok,rlst = test_calc_mincost.dotest(start_end=o.Text.encode('utf-8'),refroute=reflst, snapshot=True)
        except:
            print '测试出现崩溃'
            teskok = False
            #把整行标为红色
            sheet.Rows('%d:%d'%(line,line)).Interior.ColorIndex = 3
            sheet.Rows('%d:%d'%(line,line)).Interior.Pattern = 1
            continue
        #填充Excel
        for i in range(3,150):
            col = (cols[i]+"%d")%line
            s = '%.2f'%(float(rlst[i]['routedistance'])/1000)+'/'+'%.2f'%(float(rlst[i]['estimatetime'])/3600)
            if reflst != '' :
                s = s+'\n'+'%.2f'%(float(rlst[i+4]['routedistance'])/1000)+'/'+'%.2f'%(float(rlst[i+4]['estimatetime'])/3600)
            sheet.Range(col).FormulaR1C1 = s
            if not testok:
                #测试失败将对应表格填为黄色 
                sheet.Range(col).Interior.ColorIndex = 6
                sheet.Range(col).Interior.Pattern = 1
                sheet.Range(col).Font.Bold = True
            #插入截图到excel中
            sheet.Rows('%d:%d'%(line,line)).RowHeight = 90#为了截图调整行高
            col = (cols2[i]+"%d")%line
            fn = fixture.OutDir + ("route%d.png"%(i))
            pic = sheet.Pictures().Insert(fn)
            pic.ShapeRange.LockAspectRatio = True
            pic.ShapeRange.Height = 80
            pic.ShapeRange.Width = 140
            pic.ShapeRange.Rotation = 0
            pic.ShapeRange.Left = sheet.Range(col).Left
            pic.ShapeRange.Top = sheet.Range(col).Top
        #建立目录备份测试结果
        TestCaseNo = sheet.Range('B%d'%line).Text
        BackupDir = os.path.join(fixture.OutDir,TestName,TestTime,TestCaseNo)
        os.makedirs(BackupDir)
        for p in os.listdir(fixture.OutDir):
            f = os.path.join( fixture.OutDir, p )
            if os.path.isfile( f ):
                shutil.copyfile(f,os.path.join(BackupDir,p))

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

