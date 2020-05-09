a = [1,2,3,4]

try:  # try里面有内容报错就会跳到except中
    print(a[5])
    print("代码正常")
except:
# except IOError as e 写入文件报错
    print("代码报错了")
print("代码执行完毕")