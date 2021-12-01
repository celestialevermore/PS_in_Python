from collections import deque

test = ['a','b','c']

deq =  deque(test)
print(deq)
deq.append('d')
print(deq)


#appendleft(x)
#deque는 양방향에서 데이터를 처리할 수 있는 구조입니다.
#따라서 append(x)가 오른쪽에서 추가삽입을 해준다면,
#appendleft(x)는 왼쪽에서, 즉 앞쪽에서 추가삽입을 해주는 메소드입니다. 


print(deq)
deq.appendleft('e')
print(deq)


list2 = ['a','b','c','d']
list3 = ['a','b','c','d']
list2.append('ef')
list3.extend('ef')

print(list2,'size : ',len(list2))
print(list3,'size : ',len(list3))


##### extendleft(iterable)
# collection.deque.extendleft()는 appendleft()와 마찬가지로 왼쪽에서
# 데이터를 추가해주는 메소드입니다. 

#예제4. extendleft()

deq = deque(['a','b','c'])
deqtmp = deque(['a','b','c'])
deq.extendleft('de')
deqtmp.appendleft('de')
print(deq)
print(deqtmp)




### rotate(n)

# collection.deque.rotate(n)은 요소들을 값만큼 회전해주는 메소드입니다.
# 값이 음수이면 왼쪽으로 회전하고,
# 값이 양수이면 오른쪽으로 회전하게 됩니다.

#1회전
deq1 = deque(['a','b','c','d','e'])
deq1.rotate(1)
print(deq1)


#2회전
deq2 = deque(['a','b','c','d','e'])
deq2.rotate(2)
print(deq2)

deq3 = deque(['a','b','c','d','e'])
deq3.rotate(-1)
print(deq3)


deq4 = deque(['a','b','c','d','e'])
deq4.rotate(-2)
print(deq4)