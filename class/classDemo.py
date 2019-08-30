# 使用关键字class就可以定义一个类
# 类里面的所有属性作用域对象是类的实例或类本身
class classDemo:
    i=123123
    # 定义私有参数
    __private =0
    #类的方法和普通的函数定义一样，但是方法参数上面第一个参数要为self
    #self指的是类的实例，这个self是可以随便定义的，代表的是类的实例
    def helloworld(self):
        print("helloworld")
        print(self.__class__)
        # 类内部可以访问这个私有的属性
        print(self.__private)
    # 构造函数是指类实例化的会被执行的方法 __init__则为py中构造函数的命名
    def __init__(self,a):
        i=a
        print("构造函数开始啦")
    def __private_mathod():
        print("private_mathod") 

c=classDemo(10)
c.helloworld()
# 在类外部引用私有属性会报错
# c.__private

#继承
#py支持多继承，从左到右就可以多继承
# class classSon(classDemo,classDemo1,classDemo2):
class classSon(classDemo):
    def helloworld(self):
         print("son helloworld")

#和其他语言一样，当子类没有构造函数的时候，会自动引用父类的构造函数
c=classSon(10)
#当子类覆盖同名方法的时候使用子类的方法，当子类无法找到该方法的时候则会从继承的从左到右寻找(py支持多继承)
c.helloworld