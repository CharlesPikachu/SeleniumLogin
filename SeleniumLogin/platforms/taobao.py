'''
Function:
	淘宝网模拟登录
Author:
	Charles
微信公众号:
	Charles的皮卡丘
GitHub:
	https://github.com/CharlesPikachu
更新日期:
	2019-12-17
'''
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


'''淘宝网模拟登录'''
class Taobao():
	def __init__(self, is_headless=True, **kwargs):
		self.login_url = 'https://login.taobao.com/member/login.jhtml'
		self.chrome_options = webdriver.ChromeOptions()
		self.chrome_options.add_experimental_option('prefs', {'profile.managed_default_content_settings.images': 2})
		self.chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
		if is_headless:
			self.chrome_options.add_argument('--headless')
			self.chrome_options.add_argument('--disable-gpu')
	'''登录函数'''
	def login(self, username, password, chromedriverpath=None):
		browser = webdriver.Chrome(executable_path=chromedriverpath, options=self.chrome_options)
		visit_wait = WebDriverWait(browser, 10)
		browser.get(self.login_url)
		browser.implicitly_wait(30)
		browser.find_element_by_xpath('//*[@class="forget-pwd J_Quick2Static"]').click()
		browser.implicitly_wait(30)
		browser.find_element_by_xpath('//*[@id="TPL_username_1"]').send_keys(username)
		browser.implicitly_wait(30)
		browser.find_element_by_xpath('//*[@id="TPL_password_1"]').send_keys(password)
		browser.implicitly_wait(30)
		browser.find_element_by_xpath('//*[@id="UA_InputId"]').click()
		username_get = visit_wait.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.site-nav-bd > ul.site-nav-bd-l > li#J_SiteNavLogin > div.site-nav-menu-hd > div.site-nav-user > a.site-nav-login-info-nick ')))
		print('[INFO]: Login successfully, your username is <%s>...' % username_get)
		return username_get, browser


'''测试'''
if __name__ == '__main__':
	init_args = {'is_headless': False}
	username, browser = Taobao(**init_args).login(username='', password='', chromedriverpath='')