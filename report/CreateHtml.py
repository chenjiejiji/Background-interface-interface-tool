#coding:utf-8
import os
import time
from jinja2 import Template

class CreateHtml(object):
	def __init__(self):
		self.FilePath = './report/report/'+time.strftime('%Y%m%d%H%M%S',time.localtime())+'.html'
		self.ModorHtmlName = './report/HTML.html'

	def CreateHtml(self,datas,Amount,Succeedcount):
		ModorHtml = open(self.ModorHtmlName,'r+')
		HtmlFile = open(self.FilePath,'w+')
		data={}
		data['items'] = datas

		template = Template(ModorHtml.read().decode('UTF-8'))
		# New_html=template.render(**data)
		New_html=template.render(autonumber=Amount,successrate=Succeedcount,**data)
		HtmlFile.write(New_html.encode('UTF-8'))
		
		ModorHtml.close()
		HtmlFile.close()

		return self.FilePath