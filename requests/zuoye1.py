# 导入requests包
import requests
# 导入查询方法
from dbtools import chaxun

"""
用户登录接口
构建请求
"""
url = "http://192.144.148.91:2333/regist"  #  登录接口的地址
headers = {"Content-Type":"application/json"}
data = { "username":"15811111111","password":"15811111111","phone":"15811111111","email":"15811111111@163.com"}  #  data传递参数键值对字典方式
res = requests.post(url = url,json = data)  #  url = url1,data以json方式传送


assert res.status_code == 200  #  调用requests的status_code属性，获取http状态码
assert res.json().get("status")  == 200 #  吧返回值转换成py的字符串并断言“status”是否等于200(结果码)

sql = "select * from t_user where username = '{}'".format(data.get("username"))
assert len(chaxun(sql)) !=0
print("ok")
