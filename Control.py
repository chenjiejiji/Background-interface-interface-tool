#coding:utf-8

from libs import LibRequests
import json
from data import ReadCSV
from report import CreateHtml
import time
import os
import sys

class Control(object):
	def __init__(self):
		#get csv DATE
		self.CSVData = ReadCSV.ReadCSV()
		self.DataCSV =  self.CSVData.ReadRrturnData()
		self.dr = LibRequests.LibRequests()
		self.FileName = './Log/'+time.strftime('%Y%m%d%H%M%S',time.localtime())+'.log'
		self.WriteLog = open(self.FileName,'a+')
		self.CreateHtml = CreateHtml.CreateHtml()

	def ControlData(self):
		#get request
		Succeedcount = 0.00
		Amount = 0
		for data in self.DataCSV:
			if data['PostAndGet'].upper() == "POST" and data['Data']!="":
				Requtes = self.dr.PostRequests(data['HttpURL'],json=eval(data['Data'].replace("|",",")))
				data['Requtes'] = json.dumps(Requtes).decode("unicode-escape")
			elif data['PostAndGet'].upper() == "GET" and data['Data']!="":
				Requtes = self.dr.GetRequests(data['HttpURL'],params=eval(data['Data'].replace("|",",")))	
				data['Requtes'] = json.dumps(Requtes).decode("unicode-escape")
			else:
				data['Requtes'] = U"参数错误，请检查!!!"

			if  data['AessertDate'] in data['Requtes']:
				data['Result'] = 'T'
				Succeedcount = Succeedcount+1
			else:
				data['Result'] = 'F'

			Amount = Amount+1
			
			self.ControlLog("[HttpURL]",data['HttpURL'])
			self.ControlLog("[数据]",data['PostAndGet'])
			self.ControlLog("[请求方式]",data['PostAndGet'])
			self.ControlLog("[发送数据]",data['Data'])
			self.ControlLog("[返回结果]",data['Requtes'].encode('UTF-8'))
			self.ControlLog("[通过]",data['Result'])

		ant =  "%2.f"%((Succeedcount/Amount)*100)
		# Create HTML
		self.ControlHtml(self.DataCSV,Amount,ant)


	def ControlLog(self,TagInfo,LogInfo):
		self.WriteLog.write(TagInfo+LogInfo+TagInfo+"\n")

	def ControlHtml(self,DateHtml,Amount,Succeedcount):
		self.WriteLog.close()
		self.FileHtml = self.CreateHtml.CreateHtml(DateHtml,Amount,Succeedcount)
		os.system(sys.path[0]+self.FileHtml)
		

if __name__ == '__main__':
	Control().ControlData()