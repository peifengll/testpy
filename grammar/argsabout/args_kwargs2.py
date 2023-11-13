import functools
import logging


def test(*args, **kwargs):
    print("无指定的参数为：")
    for i in args:
        print(i)
    print("有指定的参数为：")
    for key, value in kwargs.items():
        print(key, "=", value)



test('this', 'that', item="BTC", price="20000USD")

'''
无指定的参数为：
this
that
有指定的参数为：
item = BTC
price = 20000USD
'''
