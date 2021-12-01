
N,M = map(int, input().split())

binary = list(map(int,input().split()))
binary.sort()
start=0
end=N 
mid =(start+end)//2
res=0
def BinarySearch(start, mid, end):
    if binary[mid]==M:
        
        global res
        res=mid
        #print("Get the answer",binary[mid],mid,res)
        return
    elif binary[mid]<M:
        start=mid
        end=N
        mid = (start+end)//2
        #print("start:",start,"mid:",mid,"end:",end,sep=' ')
        BinarySearch(start,mid,end)

    elif binary[mid]>M:
        end = mid
        start=start 
        mid = (start+end)//2
        #print("start:",start,"mid:",mid,"end:",end,sep=' ')
        BinarySearch(start,mid,end)



BinarySearch(start,mid,end)

print(res+1)
        