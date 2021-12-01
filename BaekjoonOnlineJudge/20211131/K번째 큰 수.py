#N,K = map(int,input().split())

#nums = [int(x) for x in input().split()]


#nums.sort()

#print(nums)

#tmp=0
#res=[]

#for i in range(len(nums)):
#    cur = nums[i]
#    #print('cur : ',cur)
#    for j in range(i+1,len(nums)):
#        next = nums[j]
#        #print('next : ',next)
#        for k in range(j+1,len(nums)):
#            end = nums[k]
#            #print('end :',end)
#            tmp = cur+next+end
#            if tmp not in res:
#                res.append(tmp)
#            #print('tmp : ',tmp)
            


#res.sort()

##print(res)
#print(res[len(res)-K])