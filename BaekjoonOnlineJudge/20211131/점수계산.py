N = int(input())

arr = list(map(int,input().split()))

score = [0]*N
flag=0

if arr[0]==1:
    score[0]=1


for i in range(1,len(arr)):
    if arr[i]==0:
        score[i]=0
    elif arr[i]==1 and arr[i-1]!=0:
        score[i]=score[i-1]+1
    elif arr[i]==1 and arr[i-1]==0:
        score[i]=1


sum_=sum(score)
print(sum_)
