def solution(start):
    ones =""
    zeros=""
    cnt=0
    for i in range(len(start)):
        ones+='1'
        zeros+='0'

    if start == ones or start == zeros:
        return 0


    while True:
        if start==ones or start==zeros:
            break
        start=start.replace('1','0')
        cnt+=1
    return cnt



test = solution('11001100110011000001')
print(test)