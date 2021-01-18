with open('admit.csv', 'r', encoding='utf-8') as f:
    ls=[]
    for i in f.readlines()[1:]:
        ls.append(i.strip().split(','))
n=input()

if n=='1':
    ls.sort(key=lambda x:x[-1],reverse=True)
    for i in range(10):
        print(ls[i])
elif n=='Research':
    a,b,c,d=0,0,0,0
    for i in ls:
        if eval(i[-1])>=0.8:
            c+=1
        elif eval(i[-1])<=0.6:
            d+=1
        if i[-2]=='1':
            if eval(i[-1])>=0.8:
                a+=1
            elif eval(i[-1])<=0.6:
                b+=1
    print('Reseach in >80%:{:.2f}%'.format((a/c)*100))
    print('Reseach in <60%:{:.2f}%'.format(100*(b/d)))
elif n=='2':
    a=0
    ld=[]
    for i in ls:
        if eval(i[-1])>=0.8:
            ld.append(i)
    for j in ld:
        a+=eval(j[1])
    print('GRE Average Score:{:.2f}'.format(a/len(ld)))
    ld.sort(key=lambda x:x[1],reverse=True)
    print('GRE Max Score:{:.2f}'.format(eval(ld[0][1])))
    ld.sort(key=lambda x:x[1],reverse=False)
    print()
    print('GRE Mix Score:{:.2f}'.format(eval(ld[0][1])))
elif n=='3':
    a=0
    ld=[]
    for i in ls:
        if eval(i[-3])>=0.8:
            ld.append(i)
    for j in ld:
        a+=eval(j[-3])
    print('GRE Average Score:{:.3f}'.format(a/len(ld)))
    ld.sort(key=lambda x:x[-3],reverse=True)
    print('GRE Max Score:{:.3f}'.format(eval(ld[0][-3])))
    ld.sort(key=lambda x:x[-3],reverse=False)
    print('GRE Mix Score:{:.3f}'.format(eval(ld[0][-3])))
else:
    print('Wrong Input')

