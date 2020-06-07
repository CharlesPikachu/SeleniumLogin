'''
Function:
	selenium模拟登录
Author:
	Charles
微信公众号:
	Charles的皮卡丘
GitHub:
	https://github.com/CharlesPikachu
更新日期:
	2020-06-07
'''
from .core import *


'''模拟登录'''
class Login():
	def __init__(self, is_headless=False, **kwargs):
		self.info = 'Login some website using selenium.'
		self.init_args = {'is_headless': is_headless}
		self.__initializeAll()
	'''初始化所有平台'''
	def __initializeAll(self):
		for key, value in {'taobao': taobao(**self.init_args).login, 
						   'bilibili': bilibili(**self.init_args).login}.items():
			setattr(self, key, value)
	'''repr'''
	def __repr__(self):
		return self.info