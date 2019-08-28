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
