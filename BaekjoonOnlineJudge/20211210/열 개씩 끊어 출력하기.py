from sys import stdin

start = input()


len = len(start)

res=[]

recnt = len//10 
endp=0
for i in range(recnt+1):
    s=10*i 
    e=s+9
    endp=e+1
    res.append(start[s:e+1])





for i in res:
    print(i)