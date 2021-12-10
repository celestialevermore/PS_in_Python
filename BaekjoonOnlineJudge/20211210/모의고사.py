def solution(answers):
    answer=[]

    p1=[1,2,3,4,5] #5
    p2=[2,1,2,3,2,4,2,5] #8
    p3=[3,3,1,1,2,2,4,4,5,5] #10

    cnt=0
    a1=0
    a2=0
    a3=0
    for i in range(len(answers)):
        if answers[i]==p1[i%5]:
            a1+=1
        if answers[i]==p2[i%8]:
            a2+=1
        if answers[i]==p3[i%10]:
            a3+=1


    tmp=[]
    tmp.append(a1)
    tmp.append(a2)
    tmp.append(a3)

    cur= max(tmp)
    for i in range(3):
        if cur==tmp[i]:
            answer.append(i+1)



    return answer




test  = solution([1,3,2,4,2])
print(test)





