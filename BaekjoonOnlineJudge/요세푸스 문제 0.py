import sys 
from collections import deque 


N,K = map(int,sys.stdin.readline().split())


persons = deque()
for i in range(1,N+1):
    persons.append(int(i))

res=[]

while persons:
    for time in range(K-1):
        tmp = persons.popleft()
        persons.append(tmp)
    
    res.append(persons.popleft())



print('<',end='')
for i in range(len(res)-1):
    print(res[i],end=', ')
print(res[-1],end='')
print('>')