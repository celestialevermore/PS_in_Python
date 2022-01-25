import sys
from collections import deque 

N = int(input())
queue = deque() 

for i in range(1,N+1):
    queue.append(i)



while len(queue)!=1:
    queue.popleft()
    next = queue.popleft()
    queue.append(next)

print(queue[0])