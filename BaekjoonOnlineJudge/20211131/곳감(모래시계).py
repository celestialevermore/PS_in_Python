##N%(N-i)+K


#test = [12,39,30,23,11]

#def switch(a,b):
#    tmp=a
#    a=b
#    b=tmp


#N = len(test)

#def modular(dir,list,N,K):
    
#    if dir==0:
#        for i in range(len(list)):
#            tmp = list[i]
#            list[i]=list[N%(N-i)+(N-K)]
#            list[N%(N-i)+(N-K)]=tmp
            
#    elif dir==1:
#        for i in range(len(list)):
#            tmp = list[i]
#            list[i]=list[N%(N-i)+(K)]
#            list[N%(N-i)+(K)]=tmp
           
    
#    return list


##res=  modular(0,test,5,3)
##print(res)


#N = int(input())

#arr = [[0 for i in range(N+1)] for j in range(N+1)]

#for i in range(1,N+1):
#    cur = list(map(int,input().split()))

#    for j in range(len(cur)):
#        arr[i][j+1]=cur[j]


#print()

#for i in range(1,N+1):
#    for j in range(1,N+1):
#        print(arr[i][j],end = ' ')
#    print()