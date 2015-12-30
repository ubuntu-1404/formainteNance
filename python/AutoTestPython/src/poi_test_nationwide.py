# coding=gbk
'''
Created on 2011-9-5
��ȫ����Χ�ڣ���ȡһ��100*100����Ȼ���ÿ��������ܱ�����
@author: Administrator
'''
import win32com.client
import traceback
import fixture
from navapp import autotest
from navapp import navitool
from testcase.poi import test_poi_correctness
import time
import os
import re
import shutil

TestName = 'poi_�ܱ�����_ȫ��'
localt = time.localtime()
TestTime = '%04d-%02d-%02d-%02d-%02d-%02d'%(localt[0],localt[1],localt[2],localt[3],localt[4],localt[5])

#fixture.connectdevice()

excel = win32com.client.Dispatch("Excel.Application")
excel.DisplayAlerts = False
filename = (fixture.SourceDir + '��������Ӧ�ò���Լ��list.xls').decode('gbk')
output = (fixture.OutDir + '��������Ӧ�ò���Լ��list_output.xls').decode('gbk')
d1 = excel.Workbooks.Open(Filename = filename)
sheet = d1.Sheets('�ܱ�����_ȫ��')

sheet.Columns('C:C').ColumnWidth = 20

#��㾭γ��
start = '8761671,4382637'
#start = '11640725,3990452'
if len(re.findall('\d+,\d+',start)) == 1:
    t = re.split(',',start)
    pos_x = t[0]
    pos_y = t[1]
    
input_name1 = sheet.Range('d4').Text.encode('gbk')
input_name2 = sheet.Range('e4').Text.encode('gbk')
input_name3 = sheet.Range('f4').Text.encode('gbk')
input_name4 = sheet.Range('g4').Text.encode('gbk')       
input_name0 = [input_name1,input_name2,input_name3,input_name4]
cols = ['D','E','F','G']
#�������excel���
line = 5
id = 1
for i in range(0,100):
    for j in range(0,100): 
        start_pos = ','.join([str(pos_x),str(pos_y)])
        index = 0
        for name in input_name0: 
            try:
                print('Calculating... ' + start_pos)     
                testok = test_poi_correctness.dotest(find_type='',districtccode = start_pos, input_name = name,input_type='') 
                print testok
                sheet.Range((cols[index]+'%d')%line).FormulaR1C1 = testok
                index = index + 1
            except RuntimeError:
                print '���Գ��ֱ���'
                teskok = False
                #�����б�Ϊ��ɫ
                sheet.Rows('%d:%d'%(line,line)).Interior.ColorIndex = 3
                sheet.Rows('%d:%d'%(line,line)).Interior.Pattern = 1
           
        sheet.Range('b%d'%line).FormulaR1C1 = id
        sheet.Range('c%d'%line).FormulaR1C1 = "'" + start_pos
        line = line + 1
        id = id + 1
        pos_x = int(pos_x) + 40000    
    pos_x = int(t[0])
    pos_y = int(pos_y) - 20000
    
    
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
shutil.copyfile(output,os.path.join(backdir , '��������Ӧ�ò���Լ��list_POI_ȫ��.xls'))          
