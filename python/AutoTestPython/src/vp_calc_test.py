# coding=gbk

'''
Created on 2011-8-22

@author: Administrator
'''

import win32com.client
import traceback
from navapp import autotest
from navapp import navitool
from testcase.vp import test_vp_recalc
import time
import fixture
import re
import os
import shutil

TestName = 'VP�����Բ���'
localt = time.localtime()
TestTime = '%04d-%02d-%02d-%02d-%02d-%02d'%(localt[0],localt[1],localt[2],localt[3],localt[4],localt[5])

fixture.connectdevice()

excel = win32com.client.Dispatch("Excel.Application")
excel.DisplayAlerts = False
filename = (fixture.SourceDir + '��������Ӧ�ò���Լ��list.xls').decode('gbk')
output = (fixture.OutDir + '��������Ӧ�ò���Լ��list_output.xls').decode('gbk')
d1 = excel.Workbooks.Open(Filename = filename)
sheet = d1.Sheets('VP������')
#Ϊ�˽�ͼ�����п�
sheet.Columns('k:k').ColumnWidth = 24

for line in range(15,16):
    o = sheet.Range('E%d'%line)
    ref = sheet.Range('F%d'%line)
    nmea = sheet.Range('G%d'%line)
    col = "K%d" % line
    if(len(o.Text)!=0) and len(ref.Text)!=0:
        print('Calculating... ' + o.Text)
        reflst = ref.Text.encode('utf-8')
        nmea1 = nmea.Text.encode('utf-8')
        try:
            testok = test_vp_recalc.dotest(start_end=o.Text.encode('utf-8'),time_span=reflst,nmea=nmea1,expect_recalc=True)
            print(testok)
            sheet.Range('I%s'%line).FormulaR1C1 = testok
        except RuntimeError:
            print '���Գ��ֱ���'
            teskok = False
            #�����б�Ϊ��ɫ
            sheet.Rows('%d:%d'%(line,line)).Interior.ColorIndex = 3
            sheet.Rows('%d:%d'%(line,line)).Interior.Pattern = 1
            continue
        
fixture.closedevice()

for i in xrange(d1.Sheets.Count,0,-1):
    if d1.Sheets(i) != sheet:
        d1.Sheets(i).Delete()
d1.Windows(1).FreezePanes = False
d1.SaveAs(output)
d1.Close()
excel = None

#���Excel��
backdir = os.path.join(fixture.OutDir , TestName, TestTime)
try:
    os.makedirs(backdir)
except:
    None
shutil.copyfile(output,os.path.join(backdir , '��������Ӧ�ò���Լ��list_VP.xls'))

