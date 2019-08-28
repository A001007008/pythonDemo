#普通的for循环
for num in range(10,15):
    print(num)
else:
    #带了else的for循环，当for循环条件不满足的时候会执行else语句
    print(1)

num=0
#while循环
while(True):
    num=num+1
    print(num)
    if num>5:
        #break语句可以终止循环，但是不会执行else语句
        break
else:
    print("执行了")      