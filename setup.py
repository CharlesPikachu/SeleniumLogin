'''
Function:
	setup
Author:
	Charles
微信公众号:
	Charles的皮卡丘
GitHub:
	https://github.com/CharlesPikachu
更新日期:
	2020-05-05
'''
import SeleniumLogin
from setuptools import setup, find_packages


'''readme'''
with open('README.md', 'r', encoding='utf-8') as f:
	long_description = f.read()


'''setup'''
setup(
	name='SeleniumLogin',
	version=SeleniumLogin.__version__,
	description='Login some website using selenium.',
	long_description=long_description,
	long_description_content_type='text/markdown',
	classifiers=[
			'License :: OSI Approved :: MIT License',
			'Programming Language :: Python :: 3',
			'Intended Audience :: Developers',
			'Operating System :: OS Independent'],
	author='Charles',
	url='https://github.com/CharlesPikachu/SeleniumLogin',
	author_email='charlesjzc@qq.com',
	license='MIT',
	include_package_data=True,
	install_requires=['selenium >= 3.141.0', 'pillow >= 6.0.0', 'numpy >= 1.16.2'],
	zip_safe=True,
	packages=find_packages()
)