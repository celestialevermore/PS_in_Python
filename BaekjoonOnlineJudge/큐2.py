from collections import deque 

N = int(input())


queue=[]

res=[]

for i in range(N):
    exc = input().split(' ')

    ex = exc[0]

    if ex=='push':
        queue.append(exc[1])
        #res.append(exc[1])

    elif ex=='pop':
        if queue:
            res.append(queue[0])
            del queue[0]
        else:
            res.append(-1)

    elif ex=='size':
        res.append(len(queue))

    elif ex=='empty':
        if queue:
            res.append(0)
        else:
            res.append(1)

    elif ex=='front':
        if queue:
            res.append(queue[0])
        else:
            res.append(-1)

    elif ex=='back':
        if queue:
            res.append(queue[-1])
        else:
            res.append(-1)


for i in range(len(res)):
    print(res[i])

