# import time
# class OldPhone:
#     __pin=""
#     def SetPin(self,pin):
#         if pin=="gsa":
#             print("没有此品牌")
#         else:
#             self.__pin=pin
#
#     def GetPin(self):
#         return self.__pin
#
#
#     def Cell(self,umber):
#         print("正在给%s带电话"%umber)
#
# class NewPhone(OldPhone):
#
#
#     def cell(self,umber):
#         print("语音拨号中")
#         for i in range(4):
#             print(".",end="")
#             time.sleep(1)
#         super().cell(umber)
#     def PhoneJ(self):
#         print("这个",self.GetPin(),"很好用")
#
#
#
# p=NewPhone()
# p.SetPin("呆鹅")
# p.Cell(159)
# p.PhoneJ()

class Cook:
    __name = ""
    __age = 0
    def setname(self,name):
        if name=="":
            print("姓名不能为空")
        else:
            self.__name = name
    def getname(self):
        return self.__name

    def setage(self,age):
        if age <= 14:
            print("你的年龄太小")
        elif age >= 140:
            print("你的年龄太大")
        else:
            self.__age = age

    def getage(self):
        return self.__age

    def zheng(self):
        print("开始蒸饭")



class  CookSon(Cook):
    def chao(self):
        print("开始炒菜")


class CookSonSon(CookSon):
    def zheng(self):
        print("蒸饭")
    def chao(self):
        print("炒菜")
    def xinxi(self):
        print("姓名", self.getname(), "年龄", self.getage())



p=CookSonSon()
p.setname('张三')
p.setage(18)
p.xinxi()
p.chao()
p.zheng()







