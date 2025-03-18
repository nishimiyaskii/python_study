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

# 继承
print('============== 继承 ==============')
class Person:
    def walk(self):
        print('我在走路')

    def eat(self):
        print('我在吃饭')

    def sleep(self):
        print('我在睡觉')

class Girl(Person):
    pass    # 如果子类没有内容，则需要一个pass占位符，用于python中的缩进
girl = Girl()
girl.walk()
girl.eat()
# 继承的传递
class LittleGirl(Girl):
    pass
little_girl = LittleGirl()
little_girl.eat()
little_girl.walk()
# 重写
print('============== 重写 ==============')
class Boy(Person):
    def walk(self):
        super().walk()  # 调用父类方法
        print('我在跑步')
    def eat(self):
        Person.eat(self)    # 调用父类方法
        print('我在吃冰棍')
    def sleep(self):
        super(Boy, self).sleep()    # 如果传入的是父类的类名，那么调用的就是父类中的重写方法
        print('我在睡午觉')
boy = Boy()
boy.walk()
boy.eat()
boy.sleep()