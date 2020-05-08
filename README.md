# SeleniumLogin
```
APIs for loginning some websites using <selenium>.
You can star this repository to keep track of the project if it's helpful for you, thank you for your support.
```

# Documents
preparing

# Support List
|  Websites        | Core Codes                                      |  in Chinese    |
|  :----:          | :----:                                          |  :----:        |
|  Bilibili        | [click](./SeleniumLogin/core/bilibili.py)       |  B站           |

# Install
#### Pip install
```
run "pip install SeleniumLogin"
```
#### Source code install
```sh
(1) Offline
Step1: git clone https://github.com/CharlesPikachu/SeleniumLogin.git@master
Step2: cd SeleniumLogin -> run "python setup.py install"
(2) Online
run "pip install git+https://github.com/CharlesPikachu/SeleniumLogin.git@master"
```

# Quick Start
#### Noted
```
To use this repo, you have to install Chrome Browser and download chromedriver from:
http://npm.taobao.org/mirrors/chromedriver/
```
#### Examples
```
from SeleniumLogin import login
lg = login.Login()
username, browser = lg.bilibili(username=xxx, password=xxx, chromedriverpath=xxx)
```

# More
#### WeChat Official Accounts
*Charles_pikachu*  
![img](pikachu.jpg)