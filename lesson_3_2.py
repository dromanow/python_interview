
class NonNegative:
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError()
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set_name__(self, owner, name):
        self.name = name


class Order:
    price = NonNegative()
    count = NonNegative()

    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count
        # self._price = price
        # self._count = count

    def total(self):
        return self.price * self.count

    # @property
    # def price(self):
    #     return self._price
    #
    # @price.setter
    # def price(self, value):
    #     if value < 0:
    #         raise ValueError()
    #     self._price = value
    #
    # def get_count(self):
    #     return self._count
    #
    # def set_count(self, value):
    #     if value < 0:
    #         raise ValueError()
    #     self._count = value
    #
    # count = property(fget=get_count, fset=set_count)


apple = Order('Apple', 5, 10)
orange = Order('Orange', 7, 2)


# order = Order('Apple', 5, -10)
# order.count = -10
# order.set_price(-20)

print(apple.total())
print(orange.total())



