# 定义一个函数
def helloworld():
    print("helloworld")


# 调用一个函数
helloworld()

# 函数可以传参数，对于基本变量，进入函数的数据对传递的数据没有影响，但是对于引用数据会产生变化


def count(a, b):
    return a+b


def count1(a, b):
    a, b = b, a
    return


print(count(10, 20))
a, b = 10, 20
count1(a, b)
print(a, b)


def count2(list):
    list[1] = 252


list = [123, 1234, 12345]
count2(list)
print(list)

# 函数中的可以传递4种参数

# 必需参数:以a,b传递，按顺序传递


def var(a, b):
    print(a, b)

# 关键字参数


def var1(a, b):
    print(a, b)


var1(b=10, a=1)

# 默认参数


def var2(a, b=35):
    print(a, b)

# 不定长参数
# 如果使用*则按元祖传递数据(多个参数会被当做一个元祖处理)


def var3(a, *b):
    print(a, b)
# 如果使用**则按字典传递数据(多个参数会被当做一个元祖处理)


def var4(a, **b):
    print(a, b)


var3(10, 10, 20, 30, 40)

var4(11, name=123, age=234)

# 声明函数时，参数中星号 * 可以单独出现,如果单独出现星号 * 后的参数必须用关键字传入
# 通配符好像不能传值


def var6(a, *, b):
    print(a, b)


var6(1, b=123)

# lambda
"""
python 使用 lambda 来创建匿名函数。

所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。

lambda 只是一个表达式，函数体比 def 简单很多。
lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
"""
#lambda [arg1 [,arg2,.....argn]]:expression
sum=lambda a,b,c:a+b+c
print(sum(10,20,30))

#return 用于结束函数和返回函数计算值
def sum1( arg1, arg2 ):
   # 返回2个参数的和."
   total = arg1 + arg2
   print ("函数内 : ", total)
   return total
 
# 调用sum函数
total = sum1( 10, 20 )
print ("函数外 : ", total)

#变量的作用域
""" Python 中，程序的变量并不是在哪个位置都可以访问的，访问权限决定于这个变量是在哪里赋值的。

变量的作用域决定了在哪一部分程序可以访问哪个特定的变量名称。Python的作用域一共有4种，分别是：

L （Local） 局部作用域
E （Enclosing） 闭包函数外的函数中
G （Global） 全局作用域
B （Built-in） 内置作用域（内置函数所在模块的范围）
以 L –> E –> G –>B 的规则查找，即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内置中找。 """

g_count = 0  # 全局作用域
def outer():
    o_count = 1  # 闭包函数外的函数中
    def inner():
        i_count = 2  # 局部作用域
        return i_count+o_count
    o_count=o_count+inner()
    return o_count
print(outer())
""" 
Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，
也就是说这些语句内定义的变量，外部也可以访问
明白这一点之后，就很好的可以理解这个变量作用域了
当引入函数之后就会引入局部作用域
同理 闭包作用域是相对于另一个函数来说的
引入模块就会产生局部作用域，相对于模块而言
 """
 #global 和 nonlocal关键字,这两个关键字可以解决以上的变量作用域问题
num = 1
def fun1():
    global num  # 需要使用 global 关键字声明,随后num的值就等同于函数外的num
    print(num) 
    num = 123
    print(num)
fun1()
print(num)

#如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了
def outer():
    num = 10
    def inner():
        nonlocal num   # nonlocal关键字声明，nonlocal作用于闭包的变量
        num = 100
        print(num)
    inner()
    print(num)
outer()
 