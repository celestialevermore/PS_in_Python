from sys import stdin 

N = int(input())

dictn = dict() 

for i in range(N):
    inputs = list(stdin.readline().split())
    
    if inputs[1]=='enter':
        if inputs[0] not in dictn:
            dictn[inputs[0]]=1
        else:
            dictn[inputs[0]]+=1
    elif inputs[1]=='leave':
        dictn[inputs[0]]-=1




resvaluelist = list(dictn.values())
reskeylist = list(dictn.keys())

#print(resvaluelist)
#print(reskeylist)

res=[]

for i in range(len(resvaluelist)):
    if resvaluelist[i]==0:
        continue
    else:
        res.append(reskeylist[i])




res.sort(reverse=True)
for i in range(len(res)):
    print(res[i])