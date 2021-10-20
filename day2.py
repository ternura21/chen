'''
猜字游戏：
需求：
1、猜的数字是系统产生的，不是自己定义的
2、键盘输入的   操作完填入：input（“提示”）
3、判断			操作完填入：if判断条件 elif 判断条件。。。。。。Else
4、循环			操作完填入：while 条件循环
#任务：开始金币有5个金币，每猜一次减一个为0就退出（or充钱）猜错3次也退出
'''
import random
#              20，10
randint=random.randint(20, 50)#随机生成数字的范围：int   []
print(randint)
j=5
i=1
l=1
while i<10:
    num = int(input("请输入您猜的数字"))
    i=i+1
    if l == 3:
        print("你已经连续错误三次，游戏失败")
        break

    if j==1:
      print("您的金币已经用完")
      break


    if num==randint:
        print("恭喜你猜对了,当前金币为",j+1)
        randint = random.randint(20, 50)  # 随机生成数字的范围：int   []
        print("新数字生成")
        j=j+1
        l=0

        # break  # 退出
    elif num>randint:
        print("猜大了,当前金币为",j-1)
        j=j-1
        l=l+1
    elif num<randint:
       print("猜小了，当前金币为",j-1)
       j=j-1
       l=l+1



