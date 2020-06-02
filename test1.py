

from jacchlibs.readxls import readxls

xls=readxls("db.xlsx")
sheet=xls.read("工作表1")  
print (sheet["A1"].value)
print (sheet["A2"].value)
print (sheet["B1"].value)
print (sheet["B2"].value)
#工作表2
#xls2=readxls("db.xlsx")
#sheet=xls.read("工作表2")
#print (sheet["A1"].value)

