from abc import abstractmethod, ABC


class A(ABC):
    # test = 10

    def __init__(self):
        pass
        # self.test = 20

    def test(self):
        self.test2()
        print('test')

    def _test(self):
        print('_test')

    def __test(self):
        print('__test')

    # @abstractmethod
    def test2(self):
        # pass
        raise NotImplementedError

    # @staticmethod
    # def fabric():
    #     return A()

    @classmethod
    def fabric(cls):
        return cls()

a = A()

# print(hasattr(a, 'test'))
# print(hasattr(a, '_test'))
# print(hasattr(a, '__test'))
# print(A.__dict__)
# print(hasattr(a, '_A__test'))

# a._A__test()


class B(A):
    pass
    # def test2(self):
    #     pass


b = B.fabric()

# print(type(b))


# a.test = lambda: print('lambda')
# a.test = 30

# A.test = 40

# print(a.__dict__)
# print(A.__dict__)
# print(a.__dict__)

# print(a.test)

setattr(a, 'test1', 50)
# print(A.__dict__)
# print(a.__dict__)

# print(getattr(a, 'test1'))


def test2(a):
    return a.test()

# test2(B())


class Animal:
    def sound_raw(self, v):
        print(v)

    def sound(self):
        self.sound_raw('Animal')


class Cat(Animal):
    def sound(self):
        print('Cat')
        super().sound()


class Dog(Animal):
    def sound(self):
        print('Dog')
        super().sound()


# MRO

#       object
#       Animal
#  Cat          Dog
#  Cat1         Dog2
#       CatDog


# Animal       Animal
#  Cat          Dog
#  Cat1         Dog2
#  Cat2
#       CatDog

# CatDog, Cat, Dog, Animal

# CatDog, Dog, Cat, Animal

# class Meta(type):
#     def mro(cls):
#         return (cls, Dog, Cat, Animal, object)



def sound_raw(self):
    print('CatDog')
    super(CatDog, self).sound()

def init_raw(self):
    self.value1 = 11


class Meta(type):
    def __new__(cls, class_name, parents, attrs, value1):
        mod_attr = {}
        for key, val in attrs.items():
            mod_attr[key] = val
            if not key.startswith('__'):
                mod_attr[key.upper()] = val
        mod_attr['value'] = value1
        print(mod_attr)
        return super().__new__(cls, class_name, parents, mod_attr)


# CatDog = Meta('CatDog', (Cat, Dog), {'sound': sound_raw, 'value': 10, '__init__': init_raw})

class CatDog(Cat, Dog, metaclass=Meta, value1=10):
    def sound(self):
        print('CatDog')
        super().sound()


class PigHorse(Cat, Dog, metaclass=Meta, value1=20):
    def sound(self):
        print('PigHorse')
        super().sound()

catdog = CatDog()
catdog.sound()
print('>>>>')
catdog.SOUND()
# catdog.value1 = 11
# print(CatDog.__dict__)
print('>>>>')
print(catdog.value)

print('>>>>')
pighorse = PigHorse()
pighorse.SOUND()
print('>>>>')
print(pighorse.value)


# print(catdog.__dict__)
# print(catdog.value1)

# print('>>>>>')
# Cat().sound()
