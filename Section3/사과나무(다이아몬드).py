#N = int(input())

#arr = [[0 for i in range(N)] for _ in range(N)]

##for i in range(N):
##    for j in range(N):
##        print(arr[i][j], end= ' ')
##    print()



#for i in range(N):
#    input_ = list(map(int,input().split()))

#    for j in range(N):
#        arr[i][j] = input_[j]


#totalsum=0

#for i in range(N):
    
#    for j in range(N):
#        totalsum+=arr[i][j]


#print(totalsum)
#subsum = 0




#def adj(i,j):
#    sum1=0
#    sum2=0
#    sum3=0
#    sum4=0
#    for i in range((N//2)):

#        for j in range((N//2)-i):
#            #좌상단
#            print(arr[i][j])
#            sum1+=arr[i][j]
#            #우하단
#            sum2+=arr[N-1-i][N-1-j]
#            #좌하단
#            sum3+=arr[N-1-i][j]
#            #우상단
#            sum4+=arr[i][N-1-j]


#    #print(sum1,sum2,sum3,sum4)
    
#    res=sum1+sum2+sum3+sum4
    
#    return res





#res = totalsum-adj(0,0)
#print(res)