def solution(numbers):
    res=0
    check=[0]*10
    
    for i in range(len(numbers)):
        check[numbers[i]]+=1

    for key,value in enumerate(check):
        if value==0:
            res+=key

    return res






inputs = [5,8,4,0,6,7,9]


test = solution(inputs)
    

print(test)
