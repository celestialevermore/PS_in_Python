
import sys 
from sys import stdin 
input = sys.stdin.readline

treedict = dict() 
treelist=[]
cnt=0 
while True:
    inputs = input().rstrip()
    if not inputs:
        break 
    else:
        treelist.append(inputs)
    cnt+=1




for tree in treelist:
    if tree not in treedict:
        treedict[tree]=1
    else:
        treedict[tree]+=1


tree_lst = list(treedict.keys())

tree_lst.sort()

for tree in tree_lst:
    print('%s %.4f' %(tree,treedict[tree]/cnt*100))

