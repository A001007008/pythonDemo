f=open("./file/file.txt",mode="w+")
""" 
可以使用open来打开一个文件，model指定读写的模式
除此以外还有一些别的参数
完整的语法格式为：
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
参数说明:
file: 必需，文件路径（相对或者绝对路径）。
mode: 可选，文件打开模式
buffering: 设置缓冲
encoding: 一般使用utf8
errors: 报错级别
newline: 区分换行符
closefd: 传入的file参数类型
opener: 
具体的参数不需要记忆，只需要在用到的时候知道就可以了
 """
#  为了读取一个文件的内容，调用 f.read(size), 这将读取一定数目的数据, 然后作为字符串或字节对象返回。
# size 是一个可选的数字类型的参数。 当 size 被忽略了或者为负, 那么该文件的所有内容都将被读取并且返回
print(f.read())

# f.readline() 会从文件中读取单独的一行。换行符为 '\n'。f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行。
print(f.readline())

# f.readlines() 将返回该文件中包含的所有行。
# 如果设置可选参数 sizehint, 则读取指定长度的字节, 并且将这些字节按行分割。
print(f.readlines())

#写入文件
num = f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
print(num)
num =f.tell()
print(num)
# 关闭
# 可以使用 with open('/tmp/foo.txt', 'r') as f 这样会自动关闭文件流(应该是流吧)
f.close()