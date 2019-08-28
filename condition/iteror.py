#任何一个集合都可以用迭代器进行遍历
list=[123,254,666,888]
it=iter(list)
#next可以获取到it的下一项
print(next(it))
for x in it :
    print(x)
