
import sys
from sys import stdin 

num = dict()
N = int(input())
inputs = list(map(int,sys.stdin.readline().split()))


for i in range(len(inputs)):
    if num[inputs[i]]==0:
        num[inputs[i]]=1
    else:

        num[inputs[i]]=1


print(num)