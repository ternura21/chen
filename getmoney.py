'''
    1.联网安装：
        python  -m   pip   install pymysql
    1.连接mysql数据库
    2.创建控制台
    3.准备sql语句
    4.执行sql语句
        4.1 增，删，改
            commit()提交即可
        4.2 查询： -->提取数据
            fetchall() 提取所有
            fetchone() 提取一个
            fetchmany(size)  提取多条
    5.提交到数据库里
    6.关闭资源
'''
# import pymysql
#
# con = pymysql.connect(host="localhost",user="root",password="",database="jason")

# 创建控制台
# cursor = con.cursor()
import  pymysql

host="localhost"
user="root"
pwd = ""
database="jason"

# 针对增，删，改
def update(sql,param):
    con = pymysql.connect(host=host,user=user,password=pwd,database=database)

    cursor = con.cursor()
    cursor.execute(sql,param)

    con.commit()
    cursor.close()
    con.close()

#
def select(sql,param,mode="all",size=0):
    con = pymysql.connect(host=host,user=user,password=pwd,database=database)

    cursor = con.cursor()
    cursor.execute(sql,param)

    if mode == "all":
        return cursor.fetchall()
    elif mode == "one":
        return cursor.fetchone()
    elif mode == "many":
        return cursor.fetchmany(size)

    con.commit()
    cursor.close()
    con.close()



# 先判断是否有账号，在判断密码对不对，再判断钱是否够
account = int(input("请输入你的账号"))
password = input("请输入你的密码")
sql = "SELECT account FROM dat WHERE account='%s'"
param = [account]
data=select(sql,param)
if len(data)==0:
    print(1)
        # return  1
else:
    sql1 = "SELECT PASSWORD FROM dat WHERE account='%s'"
    param1=[account]
    data1=select(sql1,param1)
    for i in data1:
        print(i)
        if i[0] == password:
            money1 = int(input("请输入你要取的金额"))
            sql2 = "SELECT money FROM dat WHERE account='%s'"
            param2 = [account]
            data2 = select(sql2, param2)
            for j in data2:
                if int(j[0]) >= money1:
                    sql3 = "UPDATE dat SET money=money-%s WHERE account='%s'"
                    param3 = [money1,account]
                    update(sql3, param3)
                    # return 0
                    print(0)
                else:
                    print(3)

                    # return 3

        else:
            print(2)

                # return 2























