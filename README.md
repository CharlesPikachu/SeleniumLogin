# SeleniumLogin
```
APIs for loginning some websites using <selenium>.
You can star this repository to keep track of the project if it's helpful for you, thank you for your support.
```

# Introduction in Chinese
prepare

# Support List
|  Websites        | Corresponding Codes                          |  in Chinese    |
|  :----:          | :----:                                       |  :----:        |
|  taobao          | [click](./SeleniumLogin/platforms/taobao.py) |  淘宝          |

# Noted
```
To use this repo, you have to install Chrome Browser and download chromedriver from:
http://npm.taobao.org/mirrors/chromedriver/
```

# Install
#### Use setup.py
```sh
Step1:
git clone https://github.com/CharlesPikachu/SeleniumLogin.git
Step2:
cd SeleniumLogin -> run "python setup.py install"
```
#### Use pip
```sh
pip install git+https://github.com/CharlesPikachu/SeleniumLogin.git@master
```

# Usage
#### Arguments
```
Initial Arguments:
--is_headless: True/False, whether pop-up browser or not.
Specific Loginning Arguments:
--username: your username.
--password: your password.
--chromedriverpath: the path of chromedriver downloaded in advance.
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