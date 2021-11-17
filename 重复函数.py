f=open(file="baidu_x_system.log",mode="r+",encoding="utf-8")
a=f.readlines()

# print(len(a))
f.close()


b=[]
for oneline in a:
    b.append(oneline)

# print(len(b))
#列表b是存有所有的数据

d=[]
for i in range(0,len(b)):
    # print(b[i])
    for j in range(0,len(b[i])):
        if b[i][j]==' ':
            break
    # print(j)
    c=str(b[i])[0:j:1]
    # print(c)
    d.append(str(c))
# print(d)
#已经将IP地址提取成功，提取到了列表ｄ中

# print(d)



# 方法一:

# x=y=m=n=0
# for i in d:
#     if i=='10.155.24.132':
#         x+=1
#     elif i=='16.155.34.132':
#         y+=1
#     elif i=='56.78.35.131':
#         m+=1
#     elif i == '46.76.185.36':
#         n += 1
#
# print("10.155.24.132，"
#       "16.155.34.132，"
#       "56.78.35.131，"
#       "46.76.185.36"
#       "的个数分别为",x,y,m,n)




#方法二
#利用python的collections模块下的Counter类

from collections import Counter


result=Counter(d)
print(result)




#pandas下的value_counts方法下。
# import pandas as pd
#
# result=pd.value_counts(d)
# print(result)






#方法三、
# set1=set(d)
# print(set1)   #集合不允许有重复的元素,通过集合得出列表中元素的种类和个数
# print(len(set1))