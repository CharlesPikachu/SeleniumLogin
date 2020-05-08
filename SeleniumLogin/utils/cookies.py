'''
Function:
	关于cookies的一些工具函数
Author:
	Charles
微信公众号:
	Charles的皮卡丘
GitHub:
	https://github.com/CharlesPikachu
更新日期:
	2020-05-08
'''
import json
import pickle
from selenium import webdriver


'''保存webdriver.Chrome对象的cookies'''
def saveBrowserCookies(browser, cookiespath, encoding='utf-8'):
	infos_return = {'is_success': False, 'error_info': ''}
	# browser格式不对
	if not isinstance(browser, webdriver.Chrome):
		infos_return.update({'error_info': 'Expect webdriver.Chrome in saveBrowserCookies.browser, but get %s...' % type(browser)})
		return infos_return
	# 以json格式保存
	if cookiespath.endswith('.json'):
		f = open(cookiespath, 'w', encoding=encoding)
		json.dump(browser.get_cookies(), f)
		f.close()
		infos_return.update({'is_success': True})
	# 以pikcle格式保存
	elif cookiespath.endswith('.pkl'):
		f = open(cookiespath, 'wb')
		pickle.dump(browser.get_cookies(), f)
		f.close()
		infos_return.update({'is_success': True})
	# 格式错误
	else:
		infos_return.update({'error_info': 'The format of saveBrowserCookies.cookiespath is wrong, expect json or pkl...'})
	return infos_return


'''导入cookies到webdriver.Chrome对象'''
def loadBrowserCookies(browser, cookiespath=None, encoding='utf-8'):
	infos_return = {'is_success': False, 'error_info': ''}
	# cookiespath不存在
	if not os.path.isfile(cookiespath):
		infos_return.update({'error_info': 'The loadBrowserCookies.cookiespath %s does not exist...' % cookiespath})
		return infos_return, browser
	# browser格式不对
	if not isinstance(browser, webdriver.Chrome):
		infos_return.update({'error_info': 'Expect webdriver.Chrome in loadBrowserCookies.browser, but get %s...' % type(browser)})
		return infos_return, browser
	# 导入json格式的cookies
	if cookiespath.endswith('.json'):
		f = open(cookiespath, 'r', encoding=encoding)
		for cookie in cookies:
			browser.add_cookie(cookie)
		f.close()
		infos_return.update({'is_success': True})
	# 导入pikcle格式的cookies
	elif cookiespath.endswith('.pkl'):
		f = open(cookiespath, 'rb')
		for cookie in cookies:
			browser.add_cookie(cookie)
		f.close()
		infos_return.update({'is_success': True})
	# 格式错误
	else:
		infos_return.update({'error_info': 'The format of loadBrowserCookies.cookiespath is wrong, expect json or pkl...'})
	return infos_return, browser