from sys import stdin 
from collections import deque 

deq = deque()

N,M = map(int,stdin.readline().split())
print(N,M)

#왼쪽이 음수
#오른쪽이 양수
left=0
right=0
for i in range(N):
    deq.append(i)

print(deq)


order=list(map(int,stdin.readline().split()))
for i in range(len(order)):
    order[i]-=1
print(order)

for i in range(len(order)):
    current = order[i]
    print('<<< current order :',current)
    if deq[0]==current:
        deq.popleft()
        print(deq)
    #중간보다 오른쪽에 위치해서 왼쪽연산이 유리한 경우    
    elif current > deq.index(current):
        #pass
        print('current :',current,'current left :',left)
        while True:
            print(deq)
            if deq[0]==current:
                print('executed left :',left)
                deq.popleft()
                break
            else:
                deq.rotate(1)
                left+=1

            

    #중간보다 왼쪽에 위치해서 오른쪽 연산이 유리한 경우
    elif current <= deq.index(current):
        print('current :',current,'current right :',right)
        while True:
            print(deq)
            if deq[0]==current:
                print('executed right :',right)
                deq.popleft()
                break
            else:
                deq.rotate(-1)
                right+=1

print('<<<res>>>')
print(left+right)
