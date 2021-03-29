import pandas as pd
import datetime
import csv
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\max_a\Dropbox\MAX\2018\COSMIC RAYS\Python\Vscode_work\29may.csv', sep=";", header=0,
parse_dates= {'Datetime' : [0,1]})

x = df['Datetime']
y = df['DataO']
y2= df['DataN']

plt.plot(x,y, label="Detector viejo", color ='r')
plt.plot(x, y2, label="Detector nuevo", color = 'g')

plt.xlabel("Tiempo")
plt.ylabel("Cuentas / Minuto")

plt.title ("Intensidad de Rayos Cósmicos")
plt.gcf().autofmt_xdate()
plt.legend()
plt.show()


print(df)