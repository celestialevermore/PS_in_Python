import sys
import collections 

from sys import stdin 


N = int(input())
books = []
uniques=[]
frequency=[]

for i in range(N):
    string = input()
    books.append(string)


for i in range(len(books)):
    if books[i] not in uniques:
        uniques.append(books[i])

for i in range(len(uniques)):
    books.count()
