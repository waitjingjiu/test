'''import matplotlib.pyplot as plt
import numpy as np
with open('XRD_AFO.csv', 'r', encoding='utf-8') as f:
    x,y=[],[]
    
    for i in f.readlines()[1:]:
        l=i.strip().split(',')
        x.append(eval(l[0]))
        y.append(eval(l[1]))

plt.plot(x,y,'g')
plt.xlabel('Position(2-Theta)')
plt.show()
import matplotlib.pyplot as plt
import numpy as np
if m<=eval(j[i])<=n
with open('DOSofBaTiO3PDOSTitle.csv', 'r', encoding='utf-8') as f:
    ls=[]
    
    for i in f.readlines()[1:]:
        ls.append(i.strip().split(','))
m,n=map(int,input().split())
if m>n:
    m,n=n,m
x,y=[],[]
for i in range(0,7,2):
    x=[eval(j[i]) for j in ls if m<=eval(j[i])<=n & ]
    y=[eval(j[i+1]) for j in ls if m<=eval(j[i])<=n]
    plt.plot(x,y)
    x,y=[],[]
plt.show()
'''
import matplotlib.pyplot as plt
import numpy as np
x=[10,16,13,12,7,40]
ex=[0,0.1,0,0,0,0]
lb=['a','c','java','c#','basic','py']
plt.pie(x,explode=ex,shadow=True,
        labels=lb,startangle=60,
        autopct='%2.1f%%',pctdistance=0.3)
plt.legend(loc='upper left',bbox_to_)
plt.show()
