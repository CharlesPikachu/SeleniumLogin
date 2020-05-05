# SeleniumLogin
```
APIs for loginning some websites using <selenium>.
You can star this repository to keep track of the project if it's helpful for you, thank you for your support.
```

# Documents
preparing

# Support List
|  Websites        | Core Codes                                   |  in Chinese    |
|  :----:          | :----:                                       |  :----:        |
|  taobao          | [click](./SeleniumLogin/platforms/taobao.py) |  淘宝          |

# Install
#### Pip install(preparing)
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
username, browser = lg.taobao(username=xxx, password=xxx, chromedriverpath=xxx)
```

# More
#### WeChat Official Accounts
*Charles_pikachu*  
![img](./pictures/pikachu.jpg)