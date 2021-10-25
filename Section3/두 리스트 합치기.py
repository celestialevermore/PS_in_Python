
N = int(input())
nlist = list(map(int,input().split()))

M =int(input())
mlist = list(map(int,input().split()))

res = nlist+mlist
res.sort()


for i in range(len(res)):
    print(res[i], end=' ')