import xlrd as x1
import matplotlib.pyplot as plt
import xlsxwriter
import numpy
import math
import statistics

# Reads Excel with a single time series
# no dates column, top row with series name
file = "Ibov.xls"
wb = x1.open_workbook(file)
s1 = wb.sheet_by_index(0)
r = s1.nrows
series = []
value = 0
runs = 1
print("Base de dados com",r-1,"observações")
print("para o",str(s1.cell_value(0,0)))
while runs < r:
    value = str(s1.cell_value(runs,0))
    series.append(value)
    runs = runs +1

# Calculate vol
dreturns = []
value = 0
runs = 2
while runs < r:
    value = math.log(((s1.cell_value(runs,0))/(s1.cell_value(runs-1,0))))
    dreturns.append(value)
#   print(value)
    runs = runs +1
window = dreturns[-90:]
standard = statistics.stdev(window)
root = (math.sqrt(252) * standard) * 100
format_root = "{:.2f}".format(root)
print ("Volatilidade anualizada corrente (90d) de",format_root)

# Plota evolução da vol
i=0
dmob = []
histvol = []
while i < r-91:
   dmob = dreturns[i:i+90]
   s2 = statistics.stdev(dmob)
   r2 = (math.sqrt(252) * s2) * 100
   histvol.append(r2)
   i = i + 1

# Salva histórico de vol em Excel
workbook = xlsxwriter.Workbook("EvolucaoVol.xlsx")
worksheet = workbook.add_worksheet()
runs = 1
l = len(histvol)
while runs <= l:
    worksheet.write(runs,0,histvol[runs-1])
    runs = runs + 1
workbook.close()

# Plota histórico de vol
plt.plot (histvol)
plt.show()



























