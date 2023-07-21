# 什么是迭代器？
# 迭代是访问集合元素的一种方式，迭代器是一个可以记住遍历位置的对象。
# 迭代器对象从集合的第一个元素开始访问，知道所有的元素被访问完结束。
# 迭代器只能往前不会后退
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器。
#可迭代对象不一定是迭代器，只有能用next()的叫迭代器
#可以转换为迭代器
from _collections_abc import Iterable

list1=[12,23,45,'serf']
#判断列表是否可迭代
print(isinstance(list1,Iterable))
#判断字符串是否可迭代
a='hello'
print(isinstance(a,Iterable))
#判断整数是否可迭代
i=24234
print(isinstance(i,Iterable))

#列表、字典、元组、字符串、虽然是可迭代的对象，但不是迭代器，通过next取值会报错
#print(next(list1))

#将可迭代对象转换为迭代器
g=iter(list1)

print(next(g))