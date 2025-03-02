# __del__：删除类的对象的时候，解释器会默认调用
class A:
    def __init__(self):
        print("A__init__")
    def __del__(self):
        print("A__del__")

a = A() # 创建A的对象时，__init__会立即执行
del a # 如果提前删除a对象，__del__会立即被执行
print("这是代码的最后一句") # 执行完这一句后，a对象会被回收，a中的__del__方法会自动被执行