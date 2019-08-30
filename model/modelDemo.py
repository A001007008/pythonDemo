""" 
在前面的几个章节中我们脚本上是用 python 解释器来编程，如果你从 Python 解释器退出再进入，那么你定义的所有的方法和变量就都消失了。

为此 Python 提供了一个办法，把这些定义存放在文件中，为一些脚本或者交互式的解释器实例使用，这个文件被称为模块。

模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py。模块可以被别的程序引入，以使用该模块中的函数等功能。这也是使用 python 标准库的方法。
 """
import model,sys
# 引入模块或包之前需要先将路径导入python变量中
sys.path.append("E:\python\pythonDemo")
print(sys.path)
# 引入同目录的包
model.helloworld()
# 引入不同目录的包
from function.functionDemo import var1
var1(10,20)
# 在文件夹中加入 ___init___.py文件,文件夹会被识别成包




