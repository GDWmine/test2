# 导入requests包
import requests
# 导入查询方法
from dbtools import chaxun

"""
用户登录接口
构建请求
"""
url = "http://192.144.148.91:2333/login"  #  登录接口的地址
data = {"username":"18898765432","password":"18898765432"}  #  data传递参数键值对字典方式
res = requests.post(url = url,json = data)  #  url = url1,data以json方式传送

"""
2：判断结果（http状态码；返回值信息）  断言：通过就通过，失败就报错
"""
assert res.status_code == 200  #  调用requests的status_code属性，获取http状态码
# res.status_code()
assert res.json().get("status")  == 200 #  吧返回值转换成py的字符串并断言“status”是否等于200(结果码)

"""
3：查数据库
"""
sql = "select * from t_user where username = '{}'".format(data.get("username"))
assert len(chaxun(sql)) !=0
print("ok")

token = res.json().get("data").get("token")
print(token)

"""
用户退出接口
"""

url1 = "http://192.144.148.91:2333/logout"
headers = {"Content-Type":"application/json","token":token}
res1 = requests.get(url = url1,headers = headers)
print(res1.text)
