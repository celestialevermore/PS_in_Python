import sys 
from sys import stdin

N = int(input())

grape=[0]*(N+1)
check1=[False]*(N+1)
check2=[False]*(N+1)
check3=[False]*(N+1)

cur1=3
cur2=4
cur3=4

sum1=grape[cur1-2]+grape[cur1-1]
check1[cur1-2]=True
check1[cur1-1]=True

sum2=grape[cur2-3]+grape[cur2-1]
check2[cur2-1]=True
check2[cur2-3]=True

sum3=grape[cur3-2]+grape[cur3-1]
check3[cur3-2]=True
check3[cur3-3]=True


check1[cur1]=True
check2[cur2]=True
check3[cur3]=True


for i in range(1,N+1):
    size=int(input())
    grape[i]=size 





while cur1<=N and cur2 <=N and cur3 <=N:
    if check1[cur1-2] and check1[cur1-1] and check1[cur1]:
        candi1=cur1+1
        candi2=cur1+2
        if candi1<=N and candi2<=N:
            if grape[candi1]>grape[candi2]:
                sum1+=grape[candi1]
                cur1=candi1
                check1[cur1]=True
            else:
                sum1+=grape[candi2]
                cur1=candi2 
                check1[cur1]=True
        else:
            if candi2>N:
                cur1=candi1

        
    if check2[cur2-2] and check2[cur2-1] and check2[cur2]:
        candi1=cur2+1
        candi2=cur2+2
        if candi1<=N and candi2<=N:
            if grape[candi1]>grape[candi2]:
                sum2+=grape[candi1]
                cur2=candi1
                check2[cur2]=True
            else:
                sum2+=grape[candi2]
                cur2=candi2 
                check2[cur2]=True
        else:
            if candi2>N:
                cur2=candi1

    if check3[cur3-2] and check3[cur3-1] and check3[cur3]:
        candi1=cur3+1
        candi2=cur3+2
        if candi1<=N and candi2<=N:

            if grape[candi1]>grape[candi2]:
                sum3+=grape[candi1]
                cur3=candi1
                check3[cur3]=True
            else:
                sum3+=grape[candi2]
                cur3=candi2 
                check3[cur3]=True
        else:
            if candi2>N:
                cur3=candi1



print(sum1,sum2,sum3)


