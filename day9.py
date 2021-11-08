# class watercup:
#     __higt=0
#     __rong=0
#     __cloer=""
#     __cai=""
#
#
#     # 属性的判断
#     def sethight(self,higt):
#         if higt<0 or higt>50:
#             print("您的水杯有问题")
#         else:
#             self.__higt = higt
#
#     def gethight(self):
#         return self.__higt
#
#     def setrong(self,rong):
#         if rong<0 or rong>500:
#             print("您的水杯有问题")
#         else:
#             self.__rong = rong
#     def getrong(self):
#         return self.__rong
#
#
#
#
#     # 行为......................................................
#     def cun(self):
#         print("您的水杯容量是",self.__rong,"毫升")
#
#
#
# p=watercup()
# p.setrong(280)
# p.sethight(20)
# print(p.gethight())
# p.cun()
class computer:
    __big=0
    __maney=0
    __cpu=""
    __nei=0
    __time=""

    def kansi(self):
        print("看视频，待机时间为"self.__time)
    def dazi(self):
        print("打字")
    def come(self):
        print("打游戏电脑cpu要好",self.__cpu)

