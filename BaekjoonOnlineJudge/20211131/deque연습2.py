from collections import deque


def rotate(dir,K,test):

    deq = deque(test)
    res=[]
    if dir==0:
        deq.rotate(-K)

        res = list(deq)
    else:
        deq.rotate(K)
        res=list(deq)

    return res







n = int(input())

arr = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    cur = list(map(int,input().split()))

    for j in range(n):
        arr[i][j] = cur[j]





m = int(input())
for i in range(m):
    row,dir,cnt = map(int,input().split())

    res = rotate(dir,cnt,arr[row-1])
    for j in range(len(res)):
        arr[row-1][j]=res[j]






res=0

s=0
e=n-1

for i in range(n):
    for j in range(s,e+1):
        res+=arr[i][j]
    if i<n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1


print(res)
