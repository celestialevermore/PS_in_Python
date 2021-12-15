from collections import deque
import sys
N = int(input())

executions=[]
for i in range(N):
    string = sys.stdin.readline().rstrip().split()
    executions.append(string)


#for i in range(N):
#    for ii in range(len(executions[i])):
#        print(executions[i][ii],end=' ')
#    print()

q = deque()
for i in range(len(executions)):
    ex = executions[i][0]

    if ex == 'push':
        q.append(executions[i][1])

    elif ex=='pop':
        if q:
            print(q.popleft())
        else:
            print(-1)

    elif ex=='size':
        print(len(q))

    elif ex=='empty':
        if q:
            print(0)
        else:
            print(1)

    elif ex=='front':

        if q:
            print(q[0])
        else:
            print(-1)
    elif ex=='back':
        if q:
            print(q[-1])
        else:
            print(-1)

    
        


