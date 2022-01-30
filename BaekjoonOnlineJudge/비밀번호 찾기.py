import sys
from sys import stdin 

N,M = map(int,input().split())

site = dict() 

for i in range(N):
    strs=[]
    strs = sys.stdin.readline().split()
    
    if strs[0] not in site:
        site[strs[0]]= strs[1]



res=[]

for i in range(M):
    strs = sys.stdin.readline().strip()

    res.append(site[strs])


for i in res:
    print(i)