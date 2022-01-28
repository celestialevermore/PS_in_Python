import sys
from sys import stdin 
from collections import deque 

testcase = int(input())


start=0
res=[]


while start<testcase:
    cnt = int(input())
    dd = dict()
    for i in range(cnt):
        inputs = list(sys.stdin.readline().split())
        if inputs[1] not in dd:
            
            dd[inputs[1]]=1
        else:
            dd[inputs[1]]+=1
    
    valuelist = list(dd.values())
    
    keylist = list(dd.keys())
    
    #print('key :',keylist)


    if len(dd.keys())==1:
        res.append(cnt)
    else:
        rcnt = 1 
        for i in range(len(valuelist)):
            rcnt=rcnt*(valuelist[i]+1)
        res.append(rcnt+cnt)


    start+=1



for i in range(len(res)):
    print(res[i])