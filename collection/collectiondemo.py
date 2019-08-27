#以下是一些集合相关的apidemo

#list 定义一个list只需要 用方括号初始化就可以了
#list下是带下标的课，可以通过下标来查找和更新值，list可以嵌套
list = [123,"234"]
list[1]="456"
print(list)
#可以使用del来删除列表中的元素
del list[1]
print(list)
# 获取list的长度
print(len(list))
#列表可以直接相加
list=[123,456]+[567,789]
print(list)
#判断一个数字是否在list里面
print(3 in list)
print(123 in list)
#循环输出list中的值
for x in list:
    print(x)
#一些常用如末尾添加，删除的操作可以自己查看api

#元祖
#元祖总的来说和list相差不大，但是元祖不允许修改(删除元素相关)但是可以将整个元祖删除
tuple =(123,234)
del tuple

#元祖中最主要的api(个人认为)
# tuple =(123,234,"567","789"),在诸如排序或者比较的时候，需要类型为一致(int)
tuple =(123,234)
print(max(tuple))
print(min(tuple))

tuple =("123","234","567")
print(max(tuple))
print(min(tuple))

#字典
#就是一个哈希表的集合，key：value，key：value
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
#通过直接赋予的方式可以修改当前key的value
dict['Age'] = 8               # 更新 Age
dict['School'] = "菜鸟教程"  # 添加信息

dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
 
#del 个人觉得只是单纯的将某一值->指向如/dev/null这样的地址，而不是字面意思上的删除
del dict['Name'] # 删除键 'Name'
dict.clear()     # 清空字典
del dict         # 删除字典

#set集合
""" 
集合（set）是一个无序的不重复元素序列。
可以使用大括号 { } 或者 set() 函数创建集合，
注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。 
"""
a = set('abracadabra')
b = set('alacazam')
#一个函数推导取出的x，遍历abracadabra 取出不包含a、b、c中的值
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
#增加一个元素
a.add("asdasd")
#还有一个方法，也可以添加元素，且参数可以是列表，元组，字典等，语法格式如下：
a.update(a)
print(a)
#移除一个元素
a.remove( "r" )
#移除一个元素,如果没有也不会报错
a.discard( "xxx" )