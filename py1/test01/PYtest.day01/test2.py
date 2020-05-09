a = ["1","2","3","4","5","0"]  # 序列
b = ['1','2','3','6','4','0']
c = [5,7,9,2,10]
# print("6"in a)
# print("1"in a)
# print(len(a))
# print(max(a))
# print(min(a))
# print(str(a))
# print(reversed(a))
# print(sorted(a))
# print(list(c))
# print(sum(c))
# d = []
for f in a:
    print(f)
for g , h in enumerate (a):
    print(g,h)
print("        长歌行")
verse = ["青青园中葵","朝露待日晞","阳春布德泽","万物生光辉","常恐秋节至","焜黄华叶衰",
         "百川东到海","何时复西归","少壮不努力","老大徒伤悲"]
for index,item in enumerate(verse):
    if index%2 == 0:                       # 判断是否为偶数，为偶数时不换行
        print(item+"，", end='')
    else:
        print(item+"。")                   # 换行输出
a.append("7")
print(a)