# 通过列表生成式（列表推导式），我们可以创建一个列表，但是，受到内存限制，列表容量有限。而且创建一个包含上百万个元素的列表,不仅占用很大的存储空间，如果我们只需要访问前面几个元素，那么后面绝大多数占用的空间都白白浪费了。所以，如果列表元素可以按照某种算法推荐出来，那我们是否可以在循环过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在python中，这种一边循环一边计算的机制，称为生成器（generator）


#列表推导式
list1=[i for i in range(0,11)]
print(type(list1))

#创建生成器
g=(i for i in range(0,11) if i>5)
#generator
print(type(g))
#生成器是无法直接输出的 直接输出的是<generator object <genexpr> at 0x000001CB50D450B0>
#print(g)

#取值
# print(g.__next__()) #6
# print(g.__next__()) #7
# print(g.__next__()) #8
# print(g.__next__()) #9
# print(g.__next__()) #10
# print(g.__next__()) #取不到
#如果报错StopIteration，说明生成器无法再产生值

#同样能取值
print(next(g)) #6
print(next(g)) #7
print(next(g)) #8
print(next(g)) #9
print(next(g)) #10
print(next(g)) #11