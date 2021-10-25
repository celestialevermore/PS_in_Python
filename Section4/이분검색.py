N,M = map(int,input().split())


l = list(map(int,input().split()))
l.sort()
print(l)

def BinarySearch(s,e,l):
    if len(l)==1 or len(l)==0:
        print(l)
        return
    s = 0
    m = len(l)//2
    e = len(l)
    print(l)
    print(s,m,e)
    left = l[s:m]
    right = l[m:e]

    if M in left:
        BinarySearch(0,len(left),left)
    
    elif M in right:
        BinarySearch(m,len(right),right)




BinarySearch(0,len(l),l)