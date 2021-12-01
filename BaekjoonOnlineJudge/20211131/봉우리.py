n=int(input())


arr = [[0 for i in range(n+2)] for j in range(n+2)]

for i in range(n):
    cur = list(map(int,input().split()))

    for j in range(len(cur)):
        arr[i+1][j+1] = cur[j]


#print()

#for i in range(n+2):
#    for j in range(n+2):
#        print(arr[i][j], end=' ')
#    print()


cnt =0 
for i in range(n+2):
    for j in range(n+2):
        cur = arr[i][j]

        if cur>arr[i-1][j] and cur>arr[i+1][j] and cur > arr[i][j-1] and cur > arr[i][j+1]:
            cnt+=1


print(cnt)

        
