from collections import deque 

n,m = list(map(int,input().split()))

order = list(map(int,input().split()))


deq = deque([i+1 for i in range(n)])

count=0

for x in order:
    while 1:
        if deq.index(x)==0:
            deq.popleft()
            break
        if deq.index(x)-0 <= len(deq)-deq.index(x):
            deq.append(deq.popleft())
            count+=1
        else:
            deq.appendleft(deq.pop())
            count+=1

print(count)