class Singleton(object):
    __instance = None
    __first_init = False

    def __new__(cls, age, name):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, age, name):
        if not self.__first_init:
            self.age = age
            self.name = name
            Singleton.__first_init = True

a = Singleton(18, "dongGe")
b = Singleton(8, "dongGe")


print(id(a))
#140298627282200
print(id(b))
#140298627282200

print(a.age)
#18
print(b.age)
#18

a.age = 19
print(b.age)
#19

