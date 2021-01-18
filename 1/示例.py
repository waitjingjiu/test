n=input()
ls=[]
ls1=[]
seta=set()
with open('2012-19sport.csv', 'r', encoding='utf-8') as f:
    x=f.readline()
    for i in f.readlines():
        ls.append(i.strip().split(','))
if n.isdigit()==True and 2011<=int(n)<=2019:
    for z in ls:
        if n in z:
            ls1.append(z)
    for i in ls1:
        i[0]=i[0].strip('#')
    k=int(input())
    if k>100:
        for i in ls1:
            print('{} | {} | {} | {} | {} | {} | {}'.format(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
    else:
        for i in range(k):           
            print('{} | {} | {} | {} | {} | {} | {}'.format(ls1[i][0],ls1[i][1],ls1[i][2],ls1[i][3],ls1[i][4],ls1[i][5],ls1[i][6]))
elif n.lower()=='sport':
    m=input()
    a=0
    for i in ls:
        if m in i:
            seta.add(i[-2])
    ld=list(j for j in seta)
    ld.sort()
    for z in ld:
        print('{}: {}'.format(ld.index(z)+1,z))
    k=int(input())-1
    y=ld[k]
    for i in ls:
        if y in i and m in i:
            a+=eval(i[2][1:-2])
            print('{} | {} | {} | {} | {} | {} | {}'.format(i[0][1:],i[1],i[2],i[3],i[4],i[5],i[6]))
    print('TOTAL: ${:.2f} M'.format(a))        
else:
    print('Wrong Input')
