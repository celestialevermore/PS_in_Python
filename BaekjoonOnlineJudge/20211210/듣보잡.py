
# 듣도 못한 사람 : N 

# 보도 못한 사람 : M 

N,M = map(int,input().split())

Nset = set()
Mset = set() 

for i in range(N):
    a = input() 
    Nset.add(a)


for i in range(M):
    b = input()
    Mset.add(b)



resset = set()

resset = Nset.intersection(Mset)


print(len(resset))

resset = list(resset)

resset.sort()

for i in range(len(resset)):
    print(resset[i])