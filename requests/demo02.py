# 导入requests包
import requests
# 导入查询方法
from dbtools import chaxun
"""
获取轮播图接口
1：构造请求
"""
url = "http://192.144.148.91:2333/get_title_img" #  接口地址
res = requests.get(url)  #  发送get请求并把内容赋值res

"""
2：判断结果（http状态码；返回值信息）  断言：通过就通过，失败就报错
"""
assert res.status_code == 200  #  调用requests的status_code属性，获取http状态码
# res.status_code()
assert res.json().get("status")  == 200 #  吧返回值转换成py的字符串并断言“status”是否等于200(结果码)


"""
3：查数据库
"""
# 1)获取轮播图id
for r in res.json().get("data"):
    lid = r.get("id") 
    sql = "select * from t_title_img where id = {}".format(lid)
    print(sql)
    # 2)id查询数据库
    res = chaxun(sql)   # 查询内容赋值到res中
    print(res)
    try:
        assert len(res) != 0  #  数据库中查询长度不为0证明有参数
        print("id为",lid,"的轮播图存在")
    except:
        print("id为",lid,"的轮播图不存在")
print("轮播图接口代码执行成功")
