from sys import stdin
from collections import deque

deq = deque()

N,K = map(int,input().split())

res=[]

for i in range(1,N+1):
    deq.append(i)



while deq:
    for i in range(K-1):
        cur = deq.popleft()
        deq.append(cur)
    res.append(deq.popleft())


print('<',end='')
for i in range(len(res)-1):
    print(res[i],end='')
    print(',',end=' ')
print(res[-1],end='')
print('>')