
# 新建一个类
# 定义一个Person类
class Person():
    name = "张三"      # 成员变量：类里面的变量--->属性
    hight = 180
    tizhong = 100
    sex = "男"

    # 构造方法：初始化类时的方法

    # 成员方法：类里面的方法
    # self:必须写，固定，存在的意义就是为了能够在class中调用方法
    def pao(self):
        print("人可以跑")
        print(self.sex)
        return 1 
        
#  调用类：实例化类
p = Person()        #  实例化Person这个类，返回类对象并且复制给变量“p”
print(p.name)       #  调用属性
p.pao()             #  调用方法
print(p.pao())