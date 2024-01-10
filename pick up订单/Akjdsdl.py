import requests
import json


# 跨境电商主账号
def dkjds():
    url = "http://testapi.globalston.com/trade/login"
    data = {
        "username": "dkjds",
        "password": "rt123456",
        "code": "1"
    }

    response = requests.post(url, data=data)
    result = response.json()

    if result["message"]:
        print("登录成功")
        cookies = response.cookies.get_dict()
        token = result["data"]["token"]
        return token
    else:
        print("登录失败")
        return None


# 跨境电商-子账号运营
def yy():
    url = "http://testapi.globalston.com/trade/login"
    data = {
        "username": "yy",
        "password": "Aa123456",
        "code": "1"
    }
    response = requests.post(url, data=data)
    result = response.json()
    if result["message"]:
        print("登录成功")
        cookies = response.cookies.get_dict()
        token = result["data"]["token"]
        return token
    else:
        print("登录失败")
        return None


# 跨境电商-子账号-运营2
def yu():
    url = "http://testapi.globalston.com/trade/login"
    data = {
        "username": "yu",
        "password": "Aa123456",
        "code": "1"
    }
    response = requests.post(url, data=data)
    result = response.json()
    if result["message"]:
        print("登录成功")
        cookies = response.cookies.get_dict()
        token = result["data"]["token"]
        return token
    else:
        print("登录失败")
        return None


# 跨境电商-子账号-商务
def sw():
    url = "http://testapi.globalston.com/trade/login"
    data = {
        "username": "sw",
        "password": "Aa123456",
        "code": "1"
    }
    response = requests.post(url, data=data)
    result = response.json()
    if result["message"]:
        print("登录成功")
        cookies = response.cookies.get_dict()
        token = result["data"]["token"]
        return token
    else:
        print("登录失败")
        return None

