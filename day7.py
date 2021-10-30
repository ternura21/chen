import xlrd
data=xlrd.open_workbook(filename="2020年每个月的销售情况.xlsx",encoding_override=True)
yue=0
nian=0
nian1=0
for i in range(0,12):
 table=data.sheet_by_index(i)
 for j in range(1, len(table.col(0))):
     jia = table.cell_value(j, 2)
     zon = table.cell_value(j, 4)
     day = jia * zon
     yue+=day

 yue1=len(table.col(0))-1
 nian1=yue1+nian1
 nian+=yue
print("年总销售额为%.2f元,平均每日销售额为%.2f元"%(nian,nian/nian1))
# import xlrd
# data=xlrd.open_workbook(filename="2020年每个月的销售情况.xlsx",encoding_override=True)
# yue=0
# zyue=0
# nian=0
# nian1=0
# yyue=0
# Tyue=0
# fyue=0
# pyue=0
# xyue=0
# for i in range(0,12):
#      table=data.sheet_by_index(i)
#      for j in range(1, len(table.col(0))):
#          jia = table.cell_value(j, 2)
#          zon = table.cell_value(j, 4)
#          day = jia * zon
#          yue += day
#          zyue=round(yue)
#      yue=0
#      for j in range(1, len(table.col(0))):
#          if table.cell_value(j,1)=="牛仔裤":
#              jia = table.cell_value(j, 2)
#              zon = table.cell_value(j, 4)
#              day = jia * zon
#              yue += day
#              nyue=round(yue)
#          elif table.cell_value(j,1)=="羽绒服":
#              jia = table.cell_value(j, 2)
#              zon = table.cell_value(j, 4)
#              day = jia * zon
#              yue += day
#              yyue = round(yue)
#          elif table.cell_value(j, 1) == "风衣":
#              jia = table.cell_value(j, 2)
#              zon = table.cell_value(j, 4)
#              day = jia * zon
#              yue += day
#              fyue =round(yue)
#          elif table.cell_value(j, 1) == "皮草":
#              jia = table.cell_value(j, 2)
#              zon = table.cell_value(j, 4)
#              day = jia * zon
#              yue += day
#              pyue = round(yue)
#          elif table.cell_value(j, 1) == "T血":
#              jia = table.cell_value(j, 2)
#              zon = table.cell_value(j, 4)
#              day = jia * zon
#              yue += day
#              Tyue = round(yue)
#          elif table.cell_value(j, 1) == "小西装":
#              jia = table.cell_value(j, 2)
#              zon = table.cell_value(j, 4)
#              day = jia * zon
#              yue += day
#              xyue = round(yue)
#
#
#
#      print("%s月销售额占比为%.2f%%" % (i+1, xyue/zyue))
#      print(zyue,yyue,fyue,pyue,Tyue,xyue)








