'''
Function:
	淘宝模拟登录
Author:
	Charles
微信公众号:
	Charles的皮卡丘
GitHub:
	https://github.com/CharlesPikachu
更新日期:
	2020-06-07
'''
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


'''
Function:
	淘宝模拟登录
Arguments:
	__init__:
		--is_headless: 登录时是否打开Chrome浏览器界面可视化登录过程
	login:
		Input:
			--username: 用户名
			--password: 密码
			--chromedriverpath: chromedriver.exe路径
		Return:
			--infos_return: 一些必要的信息
			--browser: 实现模拟登录之后webdriver.Chrome对象
'''
class taobao():
	def __init__(self, is_headless=False, **kwargs):
		# 用户给定的变量
		self.is_headless = is_headless
		# 一些必要的变量
		self.info = 'taobao'
		self.login_url = 'http://www.taobao.com'
		# chrome options
		self.chrome_opts = webdriver.ChromeOptions()
		self.chrome_opts.add_argument('disable-infobars')
		if is_headless:
			self.chrome_opts.add_argument('--headless')
			self.chrome_opts.add_argument('--disable-gpu')
	'''login in'''
	def login(self, username, password, chromedriverpath, **kwargs):
		# 基本设置
		browser = webdriver.Chrome(executable_path=chromedriverpath, options=self.chrome_opts)
		browser.get(self.login_url)
		driver_wait = WebDriverWait(browser, 60)
		# 点击'亲, 请登录', 进入登录界面
		button = driver_wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'h')))
		button.click()
		# 输入用户名密码
		username_sender = driver_wait.until(EC.presence_of_element_located((By.ID, 'fm-login-id')))
		username_sender.send_keys(username)
		password_sender = driver_wait.until(EC.presence_of_element_located((By.ID, 'fm-login-password')))
		password_sender.send_keys(password)
		time.sleep(2)
		# 检查是否出现了滑动验证码
		try:
			slider = browser.find_element_by_xpath("//span[contains(@class, 'btn_slide')]")
			if slider.is_displayed():
				ActionChains(browser).click_and_hold(on_element=slider).perform()
				ActionChains(browser).move_by_offset(xoffset=258, yoffset=0).perform()
				ActionChains(browser).pause(0.5).release().perform()
		except:
			pass
		# 点击登录按钮
		button = driver_wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'password-login')))
		button.click()
		# 返回必要的数据
		infos_return = {'username': username}
		return infos_return, browser
	'''repr'''
	def __repr__(self):
		return self.info


'''test'''
if __name__ == '__main__':
	taobao().login('', '', '')