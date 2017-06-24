import requests

class shortRequests(object):

	"""
		A shortcut to deal with requests
	"""

	def __init__(self, url, headers={}, params={}, datas={}):
		self.URL = url
		self.headers = headers
		self.params = params
		self.datas = datas

		self.headers = {
		    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36',
		    'Accept-Encoding': ', '.join(('gzip', 'deflate', 'br')),
		    'Accept': '*/*',
		    'Connection': 'keep-alive',
		}

	def doPost(self):
		res = requests.post(self.URL, headers=self.headers, data=self.datas)
		return res

	def doGet(self):
		res = requests.get(self.URL, headers=self.headers, params=self.params)
		return res
