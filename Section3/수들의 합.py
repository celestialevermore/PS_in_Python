N,M = map(int,input().split())

arr = list(map(int,input().split()))

print(len(arr))
start=0
end=0


cnt=0

while end < len(arr):
    if start > end:
        break
    #print('start : ',start, 'end : ',end)
    cur=0
    for i in range(start,end+1):
        
        cur+=arr[i]
    #print('current cur :',cur)

    if cur<M:
        #print("M보다 작습니다.")
        end+=1
    elif cur==M:
        #print("M과 같습니다.")
        cnt+=1
        #print("현재까지 발견된 경우의 수 : ",cnt)
        end+=1
        
    else:
        #print("M보다 큽니다")
        start+=1

print(cnt)