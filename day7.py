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






