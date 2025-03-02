 # 封装
class A:
    name = 'cx'
    __age = 28 # 隐藏属性， 只能在类中访问， 不会被继承
    _height = 187   # 私有属性，可以在当前py文件中的任意地方使用，但是不能通过import导入。也会被继承（同一个py文件）
    def introduce(self):
        print(f'my name is {A.name}, {A.__age} years old')

print(A.name)
# print(A.__age)  会报错，__类似于java中的private

# 如何访问隐藏属性？
# 方法一：私有属性的变量名实际上变成了_类名__属性名
print(A._A__age) # 通过对象也可以访问
A._A__age = 18
print(A._A__age)

# 方法二：通过类提供的方法访问
a = A()
a.introduce()

print(a._height)
print(A._height)