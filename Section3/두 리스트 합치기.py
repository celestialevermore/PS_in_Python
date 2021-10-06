
N = int(input())

arrNM=[]

arrN = list(map(int,input().split()))

M = int(input())

arrM = list(map(int,input().split()))

check = [0]*(200)


print(arrN)
print(arrM)

for i in range(len(arrN)):
    check[arrN[i]]+=1

for i in range(len(arrM)):
    check[arrM[i]]+=1


for i in range(1,N+M+2):
    if check[i]!=0:
        for j in range(check[i]):
            print(i, end=' ')