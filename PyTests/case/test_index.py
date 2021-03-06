"""
首页相关测试用例
"""
import pytest       #  管测试用例的
import requests     #  实现如何请求接口

def test_lbt():
    """
        requests的内容
    """
    url = "http://192.144.148.91:2333/get_title_img?num=3"
    res = requests.get(url)
    assert res.status_code == 200
    assert res.json().get("status") == 200

    # 数据库查询

def test_courst():
    """
        首页-获取教程
    """
    url = "http://192.144.148.91:2333/getcoures"
    res = requests.get(url)
    assert res.status_code == 200
    assert res.json().get("status") == 200