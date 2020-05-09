# 父类与子类，继承与调用

class BaBa():
    money = "500w"

    def make_money(self):
        print("爸爸有钱拿去花")

# 子类可以调用父类的属性和方法
# 重写：子类把父类的属性和方法重新实现
class ErZi(BaBa):
    # pass  #  占位符号：为了让代码不报错
    money = "500e"

    def make_money(self):
        print("儿子实现了小目标")

ez = ErZi()
print(ez.money)
ez.make_money()