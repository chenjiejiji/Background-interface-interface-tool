#coding:utf-8
import requests

class LibRequests(object):
	"""
		params=None, data=None, headers=None, cookies=None, files=None,
		auth=None, timeout=None, allow_redirects=True, proxies=None,
		hooks=None, stream=None, verify=None, cert=None, json=None
	"""
		
	def PostRequests(self,url,**kwargs):
		'''
			get requests
			kwargs.setdefault('allow_redirects', True)
			return json
		'''
		try:
			r = requests.post(url,**kwargs)
			return r.json()
		except Exception as e:
			print e
			return e
			

	def GetRequests(self,url,**kwargs):
		'''
			post requests
			kwargs.setdefault('allow_redirects', True)
			return json
		'''
		try:
			r = requests.get(url,**kwargs)
			return r.json()
		except Exception as e:
			print e
			return e
		
	def OptionsRequests(self,url,**kwargs):
		'''
			Options requests
			kwargs.setdefault('allow_redirects', True)
			return json
		'''
		r = requests.options(url,**kwargs)
		return r.json()

	def HeadRequests(self,url,**kwargs):
		'''
			Head requests
			kwargs.setdefault('allow_redirects', True)
			return json
		'''
		r = requests.head(url,**kwargs)
		return r.json()

	def DeleteRequests(self,url,**kwargs):
		'''
			Deletee requests
			kwargs.setdefault('allow_redirects', True)
			return json
		'''
		r = requests.delete(url,**kwargs)
		return r.json()

