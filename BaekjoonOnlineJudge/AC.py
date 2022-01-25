import sys 
from sys import stdin 

res=[]

T = int(input())

start=0


orders=[]
numbers=[]

inputs1 = sys.stdin.readline().strip()
print(inputs1)
orders.append(inputs1[i] for i in range(len(inputs1)))
inputs2 = sys.stdin.readline().strip()
print(inputs2)
numbers.append(inputs2[i] for i in range(len(inputs2)) if inputs2[i].isdigit())

print(orders)
print(numbers)