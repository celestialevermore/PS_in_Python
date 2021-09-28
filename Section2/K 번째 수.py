
T =int(input())

#tmp = list(map(int,input().split()))

#for i in range(len(tmp)):
#    print(tmp[i], end=' ')



res=[]

start=0
while start<T:
    
    N,s,e,k=map(int,input().split())

    tmp = list(map(int,input().split()))
    ans=[]

    for i in range(s-1,e):
        ans.append(tmp[i])
    ans.sort()
    #print(ans[k-1])
    res.append(ans[k-1])
    start+=1


for i in range(len(res)):
    print('#',end='')
    print(i+1,res[i])
