class air:
    __pin=''
    __maney=0
    def setpin(self,pin):
        if pin=="":
            print("无名之辈")
        else:
            self.__pin=pin

    def getpin(self):
        return self.__pin

    def setmaney(self,maney):
        if maney<0:
            print("做慈善，送钱")
        else:
            self.__maney=maney

    def getmaney(self):
        return self.__maney

    def kaiji(self):
        print("空调开机了。。。。")


    def over(self,time):
        for i in range(time):
            print("空调将在",time,"分钟后自动关机", end="   ")
            time-=1
    def ce(self):
        print("品牌为",self.__pin,"价格为",self.__maney)





p=air()

p.kaiji()
p.over(5)
p.setpin('王')
p.setmaney(1000)
p.ce()
