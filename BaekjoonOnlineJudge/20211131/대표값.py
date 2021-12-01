
#N = int(input())

#dict1 = {}




#arr = list(map(int,input().split()))
##print(arr)

#for i in range(len(arr)):
#    dict1[i]=arr[i]



##print('dict1 : ',dict1)

#total =0 
#for i in range(len(arr)):
#    total+=arr[i]


#tmpmean = total / N
#tmpmean2 = int(tmpmean)
#cri = tmpmean-tmpmean2
#realmean=0.
#if cri>=0.5:
#    realmean = tmpmean2+1

#else:
#    realmean = tmpmean2
######여기까지 평균을 구하는 과정임
##print(realmean)
#index=[]
#scores=[]
#gap=1000
#dict2 = {}
#for i in range(len(arr)):
#    dict2[i]=abs(realmean-arr[i])

#    if gap > abs(realmean-arr[i]):
#        gap=abs(realmean-arr[i])


# ##### 여기까지 차이를 구하는 과정이었음. 
##print(gap)

##print('dict2 : ', dict2)
#for key,value in dict2.items():
#    if value == gap:
#        scores.append(key)

##print(scores)
#res=[]
#for i in scores:
#    res.append(dict1[i])

##print(res)
#resMax=-1
#for i in res:
#    if resMax < i :
#        resMax=i
##print('resMax:',resMax)
##print(dict1)

#reskey=0
#for key,value in dict1.items():
#    if value==resMax:
#        reskey=key+1
#        break


#print(realmean, reskey)

