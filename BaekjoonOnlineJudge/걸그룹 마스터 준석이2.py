
import sys 
from sys import stdin 

N,M = map(int,input().split())

girlgroup_dict=dict() 

for i in range(N):
    
    girlgroup_name = input()
    girlgroup_count=int(input())

    if girlgroup_name not in girlgroup_dict:
        girlgroup_dict[girlgroup_name]=[]

    for x in range(girlgroup_count):
        girl = input()
        girlgroup_dict[girlgroup_name].append(girl)


girlgroup_name_list = list(girlgroup_dict.keys())
girlgroup_member_list = list(girlgroup_dict.values())

res=[]

for x in range(M):
    target = input()
    order = int(input())
    flag=0
    if order == 1:
        for x in range(len(girlgroup_member_list)):

            for y in range(len(girlgroup_member_list[x])):
                if target == girlgroup_member_list[x][y]:
                    res.append(girlgroup_name_list[x])
                    flag=1 
                    break
            if flag==1:
                break 

    elif order==0:
        for x in range(len(girlgroup_name_list)):
            if target == girlgroup_name_list[x]:
                sorted_girlgroup_name_list = sorted(girlgroup_member_list[x])
                res.append(sorted_girlgroup_name_list)


for x in res:
    if type(x) == str:
        print(x)
    elif type(x) ==list:
        for xx in range(len(x)):
            print(x[xx])
