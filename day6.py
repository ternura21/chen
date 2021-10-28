import random
print("***************************")
print("*    中国工商银行          *")
print("*     账户管理系统         *")
print("***************************")
print(" ")
print("*1、开户                   *")
print("*2、存钱                   *")
print("*3、取钱                   *")
print("*4、转账                   *")
print("*5、查询                   *")
print("*6、欢迎下次光临            *")
print("****************************")
#初始化银行
bank={}
#'Frank': {'account': 24275182, 'password': '123456', 'country': '中国', 'province': '山东', 'steert': '曹县', 'door': '001', 'money': 0, 'bank_name': '保熟银行'}
#定义一个开户银行
bank_name="保熟银行"

#定义添加到银行 定义函数元素对应元素  不是名称对名称
def bankadd(account,name,password,country,province,steert,door):
    if len(bank)>=100:
        return 3
    elif name in bank:
        return 2
    else:
        bank[name]={
            "account":account,
            "password":password,
            "country":country,
            "province":province,
            "steert":steert,
            "door":door,
            "money":0,
            "bank_name":bank_name
        }
        return 1
# 存钱
def cmoney(account):
    for i in bank:
        if bank[i]['account']==int(account):
            money=int(input("请输入存钱金额"))
            bank[i]['money']=bank[i]['money']+money
            return True
        else:
            return False

def c1money():
    name=input("请输入你的用户名")
    account=input('请输入你的银行账号')
    yan=cmoney(account)
    if yan==False:
        print("输入的银行账号不存在")
    else:
        info = '''
                         ------------个人信息------------
                         账号：%s
                         密码：*****
                         余额：%d
                         开户行：%s
                     '''
        print(info%(account,bank[name]["money"],bank_name))

def qmoney(name,password):
    if name in bank:
        if bank[name]['password']==password:
            q=input("请输入你要取的金额")
            q=int(q)
            if bank[name]['money']<q:
                return 3
            else:
                bank[name]['money'] -= q
                return 4
        else:
            return 2
    else:
        return 1


def q1money():
    name=input("请输入用户名")
    account = input('请输入您的银行账号')
    password=input("请输入您的银行账号密码")
    qyan=qmoney(name,password)
    if qyan==1:
        print("查无此号")
    elif qyan==2:
        print("密码输入错误")
    elif qyan==3:
        print("余额不足")
    elif qyan==4:
        info = '''
                                 ------------个人信息------------
                                 账号：%s
                                 密码：*****
                                 余额：%d
                                 开户行：%s
                             '''
        print(info % (account, bank[name]["money"], bank_name))



#定义用户入参
def useradd():
    account=random.randint(10000000,99999999)
    name=input("请输入您的名称")
    password=input("请输入您的密码")
    print("请输入你的详细信息")
    country=input("\t\t请输入您的国籍")#\t ==tab
    province=input("\t\t请输入您的省份")
    steert=input("\t\t请输入您的街道")
    door=input("\t\t请输入您的门牌号")
    num=bankadd(account,name,password,country,province,steert,door)
    if num ==3:
        print("本银行已满请到其他银行开户")
    elif num== 2:
        print("用户已存在")
    elif num==1:
        print("恭喜你开户成功，一下是您的相信信息")
        info = '''
                   ------------个人信息------------
                   用户名:%s
                   账号：%s
                   密码：*****
                   国籍：%s
                   省份：%s
                   街道：%s
                   门牌号：%s
                   余额：%s
                   开户行名称：%s
               '''
        # 每个元素都可传入%
        print(info % (name, account, country, province, steert, door, bank[name]["money"], bank_name))
while False==0:
    index=int(input("请输入您需要的业务"))
    if index ==1:
        print("开户")
        useradd()
        print(bank)
    elif index ==2:
        print("存钱")
        c1money()
    elif index ==3:
        print("取钱")
        q1money()
    elif index ==4:
        print("转账")
    elif index ==5:
        print("查询")
    elif index ==6:
        print("下次光临")
        break
