# 实例化一个单例
class Single(object):
    _instance = None

    def __new__(cls, *args, **kw):
        if cls._instance is None:
            # cls._instance = object.__new__(cls, *args, **kw)
            cls._instance = super(Single, cls).__new__(cls)
        return cls._instance

    def __init__(self, age):
        # self.args = args
        self.age = age
        pass


a = Single(18)
b = Single(8)
print(id(a))
print(id(b))
a.age = 19  # 给a指向的对象添加一个属性
print(b.age)  # 获取b指向的对象的age属性

