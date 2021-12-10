
def solution(lottos,win_nums):
    answer=[]
    
    first,second=0,0

    correct=0 #맞은 숫자
    wrong=0
    zcnt=0
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            correct+=1
        else:
            if lottos[i] not in win_nums and lottos[i]!=0:
                wrong+=1 # 이거 때문에 1등이 될 가능성이 없음. 
            if lottos[i]==0:
                zcnt+=1 # 이거의 개수만큼 등수를 올릴 수 있음.


    #기본 등수를 정하기
    if correct>1:
        second = 7-correct
    else:
        second=6


    #최고 등수는 1등인데, wrong의 개수 만큼 더해줘야 됨.
    first  = 1 + wrong 

    answer.append(first)
    answer.append(second)



    if wrong==0 and zcnt==0:
        return [1,1]
    else:
        return answer


    

    


test = solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19])

print(test)