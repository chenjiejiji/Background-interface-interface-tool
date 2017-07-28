#coding:utf-8

import csv

class ReadCSV(object):
	"""docstring for ReadCSV"""
	def ReadRrturnData(self):
		Lines = [Line.split(',') for Line in open('./data/reqite.csv')]
		Dates = []
		for Count in range(1,len(Lines)):
			NewDate = {}
			Line = Lines[Count]
			NewDate['name']	= unicode(Line[0],'gbk')
			NewDate['HttpURL'] = Line[1]+'://'+Line[2]+":"+Line[3]+Line[4]
			NewDate['Data'] = Line[5]
			NewDate['PostAndGet'] = Line[6]
			NewDate['AessertDate'] = Line[7]

			Dates.append(NewDate)

		return Dates
