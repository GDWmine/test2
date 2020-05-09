# 导入requests包
import requests
# """
# 获取轮播图接口
# """
# url = "http://192.144.148.91:2333/get_title_img" #  接口地址
# res = requests.get(url)  #  发送get请求并把内容赋值res
# print(res)
# print(res.text)  #  打印请求返回值：res.text就是body中的值


"""
用户登录接口
"""
url1 = "http://192.144.148.91:2333/login"  #  登录接口的地址
data = {"username":"18898765432","password":"18898765432"}  #  data传递参数键值对字典方式
res1 = requests.post(url = url1,json = data)  #  url = url1,data以json方式传送
print(res1.text)


