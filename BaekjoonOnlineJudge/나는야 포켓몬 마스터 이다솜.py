from sys import stdin 

N,M = map(int,stdin.readline().strip().split())


dictn = dict() 
listm = [] 
res=[]
dictm = dict()

for i in range(N):
    str = stdin.readline().strip()
    if str not in dictn:
        dictn[str]=i+1
        dictm[i+1]=str
 




for i in range(M):
    order  = input()

    if order.isnumeric():
        order = int(order)
        res.append(dictm[order])
    else:
        res.append(dictn[order])


for i in range(len(res)):
    print(res[i])

