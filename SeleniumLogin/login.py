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
	2019-12-17
'''
from .platforms import *


'''模拟登录'''
class Login():
	def __init__(self, is_headless, **kwargs):
		self.info = 'Login some website using selenium.'
		self.init_args = {'is_headless': is_headless}
	'''淘宝'''
	def taobao(self, username, password, chromedriverpath=None):
		return taobao.Taobao(**self.init_args).login(username, password, chromedriverpath)
	'''Info'''
	def __repr__(self):
		return self.info