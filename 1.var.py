# coding=utf-8
# -*- coding: utf-8 -*-
# 如果是解释器是python而不是python3 那么需要额外声明上述两者coding之一
"""
基本数据类型：
int 整数
float 浮点数
str 字符串
bool 布尔值

容器类型：
list 列表
tuple 元组
set 序列
dict 字典

特殊类型：
NoneType (None 类似于js中的null)
bytes
bytearray
range

其他内置类型：
complex
frozenset
enum.Enum

自定义类型：
class

命名规则：
1.只能使用英文字母、数字、下划线
2.不能以数字开头
3.不能使用关键字
4.区分大小写

较推荐snake_case命名 而不是camelCase命名
"""

a = 100
b = 123.45
c = '123'
d = '100'
e = '123.45'
f = 'hello, world'
g = True
print(float(a))         # int类型的100转成float，输出100.0
print(int(b))           # float类型的123.45转成int，输出123
print(int(c))           # str类型的'123'转成int，输出123
print(int(c, base=16))  # str类型的'123'按十六进制转成int，输出291
print(int(d, base=2))   # str类型的'100'按二进制转成int，输出4
print(float(e))         # str类型的'123.45'转成float，输出123.45
print(bool(f))          # str类型的'hello, world'转成bool，输出True
print(int(g))           # bool类型的True转成int，输出1
print(chr(a))           # int类型的100转成str，输出'd' 用于unicode码点值转换成具体文本 character的缩写
print(ord('d'))         # str类型的'd'转成int，输出100 用于具体文本获取对应的unicode码点值 ordinal的缩写
