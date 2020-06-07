'''
Function:
	Bilibili模拟登录
Author:
	Charles
微信公众号:
	Charles的皮卡丘
GitHub:
	https://github.com/CharlesPikachu
更新日期:
	2020-05-08
'''
import io
import time
import base64
import selenium
import numpy as np
from PIL import Image
from selenium import webdriver
from ..utils.tracks import TrackGenerator
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


'''
Function:
	Bilibili模拟登录
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
class bilibili():
	def __init__(self, is_headless=False, **kwargs):
		# 用户给定的变量
		self.is_headless = is_headless
		# 一些必要的变量
		self.info = 'bilibili'
		self.login_url = 'https://passport.bilibili.com/login'
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
		# 输入用户名密码并点击登录按钮
		username_sender = driver_wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="login-username"]')))
		username_sender.send_keys(username)
		password_sender = driver_wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="login-passwd"]')))
		password_sender.send_keys(password)
		button = driver_wait.until(EC.presence_of_element_located((By.XPATH, '//a[@class="btn btn-login"]')))
		button.click()
		time.sleep(3)
		# 获得验证码原图和带缺口的图
		image_ori = browser.execute_script('return document.getElementsByClassName("geetest_canvas_fullbg")[0].toDataURL("image/png");')
		image_ori = image_ori.split(',')[1]
		image_ori = base64.b64decode(image_ori)
		image_ori = Image.open(io.BytesIO(image_ori))
		image_gap = browser.execute_script('return document.getElementsByClassName("geetest_canvas_bg")[0].toDataURL("image/png");')
		image_gap = image_gap.split(',')[1]
		image_gap = base64.b64decode(image_gap)
		image_gap = Image.open(io.BytesIO(image_gap))
		# 找到两张图不同
		gap_pos = []
		for i in range(image_ori.size[0]):
			if gap_pos:
				break
			for j in range(image_ori.size[1]):
				pixel_ori = image_ori.getpixel((i, j))
				pixel_gap = image_gap.getpixel((i, j))
				if abs(pixel_ori[0] - pixel_gap[0]) > 10 and abs(pixel_ori[1] - pixel_gap[1]) > 10 and abs(pixel_ori[2] - pixel_gap[2]) > 10:
					gap_pos = [i, j]
					break
		distance = gap_pos[0]
		# 将滑块移动到缺口位置
		slider = driver_wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div[6]/div/div[1]/div[2]/div[2]')))
		ActionChains(browser).click_and_hold(on_element=slider).perform()
		tracks = TrackGenerator.getTracksByAcceleration(distance * 0.93)
		for delta_dis in tracks:
			ActionChains(browser).move_by_offset(xoffset=delta_dis, yoffset=0).perform()
		ActionChains(browser).pause(0.5).release().perform()
		# 返回必要的数据
		print('[INFO]: Account -> %s, login successfully...' % username)
		infos_return = {'username': username}
		return infos_return, browser
	'''repr'''
	def __repr__(self):
		return self.info


'''test'''
if __name__ == '__main__':
	bilibili().login('', '', '')