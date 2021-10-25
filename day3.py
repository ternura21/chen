# i=0
# while i<10:
#     i=i+1
#     ag=int(input("请输入需要相加的数字"))
#     if  i==1:
#         a1=ag
#
#     else:
#
#      ag=ag+a1
#
#     print("相加的和为",ag)
#     a1=ag

#
# i=0
# while i<10:
#     i=i+1;
#     usm=int(input("请输入"))
#     if i==1:
#        b1=usm
#
#        a1 = usm
#        print("最大值为", usm, "和为", usm, "平均数为", usm)
#     elif i>=2:
#         if a1>usm:
#
#             usm =b1+usm
#             print("最大值为", a1, "和为", usm,"平均数为",int(usm/i))
#             b1 = usm
#         elif a1<usm:
#             a1 = usm
#             usm=b1+usm
#             print("最大值为", a1, "和为", usm,"平均数为",int(usm/i))
#             b1 = usm
#
#         elif a1==usm:
#
#             usm = b1 + usm
#             print("最大值为", a1, "和为", usm,"平均数为",int(usm/i))
#             b1 = usm
# i=20
# a=1
# while True:
#     if 3*a-2*(a-1)==i:
#         break
#     elif 3*a-2*a==i:
#         break
#     a=a+1
# print("青蛙爬出需要",a)

# import random
# a=random.randint(50,150)
# print(a)


# a=int(input("请输入三角形的边"))
# b=int(input("请输入三角形的边"))
# c=int(input("请输入三角形的边"))
#
# if a>=b+c or b>=a+c or c>=a+b:
#     print("不能形成三角形")
# elif a==b==c:
#     print("为等边三角形")
# elif a==b and a!=c:
#     print("等腰")
# elif a==c and  a!=b:
#     print("等腰")
# elif b==c and  a!=b:
#     print("等腰")
# elif a!=b!=c:
#     print("普通三角形")
# t=input("点击加号进行调换")
# a=56
# b=78
#
# while True:
#
#     if t == "+":
#         a, b = b, a
#         print("A=",a, "B=",b)
#         input("点击减号进行调换")
#     elif t == "-":
#         b, a = a, b
#         print("A=",a, "B=",b)
#         input("点击加号进行调换")
# a=input("请输入用户名")
# b=input("请输入密码")
# i=0
# while True:
#     i=i+1
#     if a=="root"and b=="admin":
#         print("登陆成功")
#         break
#     elif a!="root"and b!="admin":
#         if i<3:
#             print("登录失败")
#             a = input("请输入用户名")
#             b = input("请输入密码")
#         elif i==3:
#             print("登录失败。账户锁定")
#             break





















