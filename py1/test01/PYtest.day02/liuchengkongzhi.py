# 流程控制：
#             三种：
#             1.条件/分支流程控制
#                 if 条件一：
#                     111111
#                 else if 条件二：
#                     222222
#                 elif 条件三：
#                     333333
#                 else：
#                     444444
# -*- coding:utf-8 -*-
# print("---------------------------------------------------if--------------------------------------------")
# """
# 90-100      A
# 80-89       B
# 70-79       C
# 60-69       D
#
# """
# score = input("请输入考试成绩：")
# score_int = int(score)
#
# if score_int>=90 and score_int<=100:
#     print("A")
# elif score_int >= 80 and score_int < 90:
#     print("B")
# elif score_int >= 70 and score_int < 80:
#     print("C")
# elif score_int >= 60 and score_int < 70:
#     print("D")
# else:
#     print("不及格")
print("---------------------------------------------------while--------------------------------------------")
# 条件为真时执行下一步代码，然后在跟条件做对比直到不满足条件跳出循环
# 使用一个循环需要满足三个条件：
# 1.开始条件
# 2.迭代条件
# 3.终止条件
#
# range(start,end,step)
#       开始，结束，步长
# range(0,10,)
# for x in range(1,10,2):
#     print(x)

"""

设定一个数值取值范围1-1000，通过编程确定设定数字并给出提示

"""
# score = input("请输入一个取值范围为1-1000的数字：")
# score_int = int(score)

# 开始条件
start = 1
# 结束条件
end = 100
# 迭代条件：number = number + 1
number = start
# 退出条件
last_result = 0
while number <= end:
    print("number1=",number)
    last_result = last_result + number
    number = number + 1
    print("number2=",number)
    print("last_result=",last_result)
