#每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
#在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。
#等号（=）用来给变量赋值
count = 10+10 #(int 类型)，py3之后就没有long类型了
print (count)

msg ="123132" #字符串

doub =100.01
print(doub)

bool,bool1,bool2,bool3 =0,1,False,True
print(bool,bool1,bool2,bool3)

#初次以外，python支持多项赋值，如上面boolen的赋值
a=b=c=1
#对于我来说这是一个诡异的操作
print(a,b,c)

'''
Python3 支持 int、float、bool、complex（复数）。

在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。

像大多数语言一样，数值类型的赋值和计算都是很直观的。

内置的 type() 函数可以用来查询变量所指的对象类型。
'''
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))

#可以通过del删除一些对象的引用
del a
#删除之后以下语句会报错，应该只是删除了a->20这一个引用，并非直接回收
#print(a)

#集合
#与字符串相同,0代表第一个，-1代表最后一个
#相同的运算可以取出对应的元素
#由于没有类型这一说法，所有一个集合里面是可以存放任意类型的元素
#list 里面可以包含list
list =["123",123,123.0,123+2j]
list2 = ["456",456,list]
print(list)
print(list+list2)
#和字符串不同的是，可以对某一元素进行修改
list2[1]="123123"
print(list2)
#除此以外，可以对某一个区间取步长值
#这一段代码显示的从0->4这个区间里面，取2个元素(步长)，如果第三个参数为负数则负向读取
print(list[0:3:2])
print(list+list2)
print(list+list2[0:4:-5])

#元祖
#元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。
tuple=(123,"2341","666",12.0)
print(tuple)
tuple=() #空数组
print(tuple)
tuple=(123,) #包含一个元素
print(tuple)
'''
1、与字符串一样，元组的元素不能修改。
2、元组也可以被索引和切片，方法一样。
3、注意构造包含 0 或 1 个元素的元组的特殊语法规则。
4、元组也可以使用+操作符进行拼接。
'''

#set集合
'''
集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。

基本功能是进行成员关系测试和删除重复元素。

可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
'''

set1={"tom","jerry","dog","cat"}
print(set)
if "tom" in set1:
    print("tom in set")
else:
    print("tom in not set")

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a - b)     # a 和 b 的差集
 
print(a | b)     # a 和 b 的并集
 
print(a & b)     # a 和 b 的交集
 
print(a ^ b)     # a 和 b 中不同时存在的元素

#字典
'''
字典（dictionary）是Python中另一个非常有用的内置数据类型。

列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。

字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。

键(key)必须使用不可变类型。

在同一个字典中，键(key)必须是唯一的。
'''
dict ={}
dict['abc']='def'
print(dict['abc'])