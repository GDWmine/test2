"""
登录相关测试用例
"""
import pytest       #  管测试用例的
import requests     #  实现如何请求接口


def test_login():
    url = "http://192.144.148.91:2333/login" 
    data = {"username":"15888888888","password":"15888888888"}
    res = requests.post(url = url,json = data)
    assert res.status_code == 200
    assert res.json().get("status") == 200
    #  保存token：存到TXT中：用py实现读写
    with open("./token.txt","w") as f:
        token = res.json().get("data").get("token")
        f.writelines(token)
def test_logout():
    """
        获取token
    """
    with open("./token.txt","r") as f:
        token = f.read()
    url = "http://192.144.148.91:2333/logout"
    headers = {"Content-Type":"application/json","token":token}
    res = requests.get(url = url,headers = headers)    
    assert res.status_code == 200
    assert res.json().get("status") == 200