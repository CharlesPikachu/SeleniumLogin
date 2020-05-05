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
	2020-05-05
'''
from .platforms import *


'''模拟登录'''
class Login():
	def __init__(self, is_headless=True, **kwargs):
		self.info = 'Login some website using selenium.'
		self.init_args = {'is_headless': is_headless}
		self.__initializeAll()
	'''初始化所有平台'''
	def __initializeAll(self):
		self.taobao = taobao(**self.init_args).login
	'''repr'''
	def __repr__(self):
		return self.info