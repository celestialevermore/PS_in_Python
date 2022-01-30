import sys 
from sys import stdin 

N = int(input())

numbers=dict()

for i in range(N):
    inputs = int(input())

    if inputs not in numbers:
        numbers[inputs]=1
    else:
        numbers[inputs]+=1


res= []

numkeys=list(numbers.keys())
numvalues = list(numbers.values())

maxvalues = max(numvalues)

minn=pow(2,63)

for i in range(len(numkeys)):
    if numbers[numkeys[i]]==maxvalues:
        minn=min(numkeys[i],minn)




print(minn)

        
