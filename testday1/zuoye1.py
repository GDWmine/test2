import time


"""
作业1
"""

# xx = ["张三","李四","王麻子","浪晋","流云","希希","小梁","二狗","陈平安","朱珠","亚索"]
# a = {}
# b = {}
# for i in range(0,len(xx),1):
#     print(xx[i])
#     x = int(input("请输入成绩:"))
#     if x > 60:
#         a[xx[i]] = x
#     else:
#         b[xx[i]] = x
# print("成绩大于60的学生",a)
# print("成绩小于60的学生",b)

# studentlist = ["张三","李四","王麻子","浪晋","流云","希希","小梁","二狗","陈平安","朱珠","亚索"]
# hight = {}
# low = {}
# for i in studentlist:
#     chengji = int(input("请输入"+i+"的成绩："))
#     if chengji >= 60:
#         hight[i] = chengji 
#     else:
#         low [i] = chengji
# print(hight,low)


"""
作业2
"""

# for i in range(1,69,1):
#     if i < 31:
#         print("红灯",end = "   ")
#     elif i < 66:
#         print("绿灯",end = "  ")
#     else:
#         print("黄灯",end=" ")
"""
遍历字典时打印key
"""
# light = {"红灯":30,"绿灯":35,"黄灯":3}
# for i in light:
#     # print(i,light[i])
#     for j in range(light[i]):
#         print(i,"倒计时还剩下：",light[i]-j,"s")