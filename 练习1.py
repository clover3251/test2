# add this line.
# class Desc:
#     def __init__(self, key, expected_type):
#         self.key = key
#         self.expected_type = expected_type
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.key]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, self.expected_type):
#             raise TypeError("输入的类型错误，{}必须是{}".format(self.key, self.expected_type))
#         instance.__dict__[self.key] = value
#
#     def __delete__(self, instance):
#         del instance.__dict__[self.key]
#
# def decorator(**kwargs):
#     def sub(obj):
#         for key, val in kwargs.items():
#             setattr(obj, key, Desc(key, val))
#         return obj
#     return sub
#
# @decorator(name=str, age=int, salary=float)  #Test=sub(Test)
# class Test:
#     # name = Desc("name", str)
#     # age = Desc("age", int)
#     # salary = Desc("salary", float)
#
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
#
#     def info(self):
#         print("{}今年{}岁，工资{}".format(self.name, self.age, self.salary))
#
#
# t = Test("Tom", 18, 8888.)
# t.info()
# print(t.__dict__)


# class MyProperty:
#     def __init__(self, obj):
#         self.obj = obj
#
#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#         return self.obj(instance)
#
# class Room:
#     def __init__(self, type, length, width):
#         self.type = type
#         self.length = length
#         self.width = width
#
#     @MyProperty
#     def area(self):
#         return self.length * self.width
#
# r1 = Room("一室一厅", 6, 5)
# r2 = Room("三室两厅", 9.6, 12)
# print(r1.area)
# print(r2.area)


class MyClassmethod:
    def __init__(self, obj):
        self.obj = obj

    def __get__(self, instance, owner):
        def sub():
            return self.obj(owner)
        return sub

class MyStaticmethod:
    def __init__(self, obj):
        self.obj = obj
    def __get__(self, instance, owner):
        return self.obj

class Desc:
    def __init__(self, key, key_type):
        self.key = key
        self.key_type = key_type

    def __get__(self, instance, owner):
        return instance.__dict__[self.key]

    def __set__(self, instance, value):
        if not isinstance(value, self.key_type):
            raise TypeError("{}必须是{}".format(self.key, self.key_type))
        instance.__dict__[self.key] = value

def decorator(**kwargs):
    def sub(obj):
        for key, val in kwargs.items():
            setattr(obj, key, Desc(key, val))
        return obj
    return sub

@decorator(name=str, source=int)
class Game:
    top_source = 0
    # name = Desc("name", str)
    def __init__(self, name, source):
        self.name = name
        self.source = source
        print("{}请游戏开始：".format(self.name))

    def player(self):
        print("{}的分数是：{}".format(self.name, self.source))
        if self.source > Game.top_source:
            Game.top_source = self.source

    @MyClassmethod
    def history(cls):
        print("历史最高分是：{}".format(cls.top_source))

    @MyStaticmethod
    def end():
        print("游戏结束")

try:
    p1 = Game("Tom", 70)
    p1.player()

    p2 = Game("Jack", 80)
    p2.player()

    p3 = Game("Rose", 90)
    p3.player()
except TypeError as f:
    print(f)

Game.history()
Game.end()

