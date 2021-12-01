start=[]
for i in range(1,21):
    start.append(i)


for i in range(10):
    a,b = map(int,input().split())
    #print(start[a-1],start[b-1])
    tmp=[]
    for j in range(a-1,b):
        tmp.append(start[j])
    #print('origin tmp:',tmp)
    tmp.reverse()
    #print('reversed tmp:',tmp)
    for k in range(len(tmp)):
        start[a-1+k]=tmp[k]
    #print(start)


for i in range(len(start)):
    print(start[i],end=' ')