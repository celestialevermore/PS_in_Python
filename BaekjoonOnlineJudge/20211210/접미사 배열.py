str = input()

res=[]



for i in range(len(str)):
    cur = i
    tmp=''
    for ii in range(cur,len(str)):
        tmp+=str[ii]
    res.append(tmp)



res.sort()

for i in res:
    print(i)