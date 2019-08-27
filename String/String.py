#py的字符串相关的demo
str ="myhomie"
#python下的字符串拼接可以直接通过[index，index来标记]
#0为正数开始，-1为负数开始
print(str[0:-5])
print(str[1:5])
#字符串拼接,+被运算符重载了
print(str+"123")
#输出两次
print(str*2) 
# 使用反斜杠(\)+n转义特殊字符
print('hello\nrunoob')
# 在字符串前面添加一个 r，表示原始字符串，不会发生转义      
print(r'hello\nrunoob')     
