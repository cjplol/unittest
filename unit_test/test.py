from calc import count
import unittest

"""
unittest是python的单元测试框架，不需要安装直接导入使用即可
测试用例类需要继承unittest.TestCase
属性该类的测试用例其实就是一个实例方法
该测试用例方法，必须要使用test开头
"""

class CountTest(unittest.TestCase):
    
    def test_add(self):
        #类的实例化
        c=count(4,5)
        #测试的本质永远是实际结果和需求结果的比较
        #断言
        self.assertEqual(c.add(),9)
    
    def test_subtraction(self):
        f=count(9,8)
        self.assertEqual(f.Subtraction(),1)

if __name__=="__main__":
    #执行测试用例（执行该测试类下面的所有测试用例）
    unittest.main()
    # c=CountTest()
    # c.test_add()