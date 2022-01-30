import sys 
from sys import stdin 

N,M = map(int,input().split())


girlgroupdict=dict() 



for i in range(N):

    
    girlgroup_name=sys.stdin.readline().strip()
    girlgroup_num = int(input())

    if girlgroup_name not in girlgroupdict:
        girlgroupdict[girlgroup_name]=[]
    girlgroup_list=[]
    for n in range(girlgroup_num):
        girlgroup_list.append(sys.stdin.readline().strip())
    girlgroupdict[girlgroup_name]=girlgroup_list


res=[]


girlgroupname = list(girlgroupdict.keys())
girlgroupmember = list(girlgroupdict.values())



for i in range(M):
    target = input()
    order = int(input())
    flag=0
    if order == 1:
        for n in range(len(girlgroupmember)):
            for m in range(len(girlgroupmember[n])):
                if target ==girlgroupmember[n][m]:
                    res.append(girlgroupname[n])
                    flag=1
                    break
            if flag==1:
                break 
    elif order==0:
        res.append(girlgroupdict[target])


for i in res:
    if type(i)==str:
        print(i)
    elif type(i)==list:
        i = sorted(i)
        for ii in i:
            print(ii)
