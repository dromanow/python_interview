# динамическая, строгая, неявная утинная

# a = 1 + 1.2
# print(a)
#
#
# # if not []:
# #     print('true')
#
#
# # print(bool(1))
# print(bool([{}]))
#
# # print(float(True))
#
# a: int = 1
#
# a = 'test'
# print(a)

# from typing import Final
#
# a: Final = 1
#

# a = [1, 2]
a = 1
# print(id(a))


def f(b):
    len = lambda a: a*2
    a = a + 2

    # def f1():
    #     nonlocal a
    #     a = 3
    #
    # print(a)  # 2
    # f1()
    # print(a)  # 3

    # print(a)
    # a = 2
    # print(id(b))
    # b[0] = 2
    # # b = 2
    # print(id(b))


f(a)
print(a)
f(a)
print(a)
f(a)
print(a)


class A:
    v = 1


_a = A()
_b = A()



_a.v = 2

import json

json.dumps()


# print(a)

# [ 2 ]
# [ 2 ] <--- []

# a = {
#     1: lambda _a: _a*_a,
#     2: lambda _a: _a*3,
# }
#
# print(a[1](2))

#
#
#
#
# if a == 1:
#     pass
# elif a == 2:
#     pass
# else:
#     pass


# int
# float
# str
# bool
# list
# tuple
# dict
# set
# frozenset
# complex
# None



