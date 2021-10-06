
N = int(input())

arr = [[0 for i in range(N)] for _ in range(N)]



for i in range(N):
    tmp = list(map(int,input().split()))
    #print(tmp)
    for j in range(N):
        arr[i][j] = tmp[j]


##print()
#for i in range(N):
#    for j in range(N):
#        print(arr[i][j], end= ' ')
#    print()


max=0

#열의 합

for i in range(N):
    col=i
    cur=0
    for j in range(N):
        cur+=arr[j][col]
    #('cur : ',cur)
    if max < cur:
        max=cur


#횡의 합

for i in range(N):
    row = i
    cur=0
    for j in range(N):
        cur+=arr[row][j]
   # print('cur : ',cur)
    if max < cur:
        max = cur


curr1=0
curr2=0
#왼우 대각선의 합
for i in range(N):
    cur1=0
    cur2=0
    cur1+=arr[i][i]
    cur2+=arr[N-1-i][i]
    curr1+=cur1
    curr2+=cur2
    #print('cur1 :',cur1,'cur2 :',cur2)
  

if max < curr1:
    max = curr1
if max < curr2:
    max = curr2

print(max)
    

