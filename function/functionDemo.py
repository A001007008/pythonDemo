#定义一个函数
def helloworld():
    print("helloworld")
#调用一个函数
helloworld()

#函数可以传参数，对于基本变量，进入函数的数据对传递的数据没有影响，但是对于引用数据会产生变化
def count(a,b):
    return a+b

def count1(a,b):
    a,b=b,a
    return
print(count(10,20))
a,b=10,20
count1(a,b)
print(a,b)

def count2(list):
    list[1]=252

list=[123,1234,12345]
count2(list)
print(list)

#函数中的可以传递4种参数

#必需参数:以a,b传递，按顺序传递
def var(a,b):
    print(a,b)

#关键字参数
def var1(a,b):
    print(a,b)

var1(b=10,a=1)

#默认参数
def var2(a,b=35):
    print(a,b)

#不定长参数
#如果使用*则按元祖传递数据
def var3(a,*b):
    print(a,b)
#如果使用**则按字典传递数据
def var3(a,**b):
    print(a,b)


