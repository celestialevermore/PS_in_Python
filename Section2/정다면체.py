N,M = map(int,input().split())

Nlist=[]
Mlist=[]

for i in range(N):
    Nlist.append(i+1)

for i in range(M):
    Mlist.append(i+1)


#print(Nlist)
#print(Mlist)
arrNM = [[i+1 for i in range(M)] for j in range(N)]

#for i in range(N):
#    for j in range(M):
#        print(arrNM[i][j], end=' ')
#    print()

for i in range(N):
    for j in range(M):
        arrNM[i][j]=i+1+j+1

res=[]
for i in range(1,401):
    res.append(0)
#크기를 늘려줘야함

for i in range(N):
    for j in range(M):
        res[arrNM[i][j]]+=1

max=-1
for i in range(len(res)):
    if max <=res[i]:
        max = res[i]

ress=[]

#내가 원래 하던 방식
#for i in range(len(res)):
#    if max==res[i]:
#        ress.append(i)

#for i in range(len(ress)):
#    print(ress[i], end=' ')

#이제 앞으로 익숙해져야 할 방식
for idx,value in enumerate(res):
    if max == value:
        ress.append(int(idx))

for i in range(len(ress)):
    print(ress[i], end=' ')