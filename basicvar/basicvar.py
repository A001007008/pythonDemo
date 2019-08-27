#每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
#在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。
#等号（=）用来给变量赋值
count = 10+10
print (count)

msg ="123132"

doub =100.01
print(doub)

bool,bool1,bool2,bool3 =0,1,False,True
print(bool,bool1,bool2,bool3)

#初次以外，python支持多项赋值，如上面boolen的赋值
a=b=c=1
#对于我来说这是一个诡异的操作
print(a,b,c)