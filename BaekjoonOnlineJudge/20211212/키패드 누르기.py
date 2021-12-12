import math

def solution(numbers,hand):
    answer=''
    mapp={
        1:[0,0],
        2:[0,1],
        3:[0,3],
        4:[1,0],
        5:[1,1],
        6:[1,2],
        7:[2,0],
        8:[2,1],
        9:[2,2],
        0:[3,1]
    }
    #초기시작
    Lpos=[[3,0]]
    Rpos=[[3,2]]

    for i in range(len(numbers)):
        target = numbers[i]
        targetx,targety=0,0
        #1을 눌러야 하는 상황
        if target==1 or target==4 or target==7:
            targetx,targety = mapp[target][0],mapp[target][1]
            answer+='L'
            Lpos.append([targetx,targety])
        
        elif target==3 or target==6 or target==9:
            targetx,targety = mapp[target][0],mapp[target][1]
            answer+='R'
            Rpos.append([targetx,targety])

        elif target==2 or target==5 or target==8 or target==0:
            #목적 좌표
            targetx,targety = mapp[target][0],mapp[target][1]

            Lcurx,Lcury = Lpos[-1][0],Lpos[-1][1]
            Rcurx,Rcury = Rpos[-1][0],Rpos[-1][1]



            Lres = abs(targetx-Lcurx)+abs(targety-Lcury)
            Rres = abs(targetx-Rcurx)+abs(targety-Rcury)

            if Lres < Rres:
                answer+='L'
                Lpos.append([targetx,targety])
            elif Rres < Lres:
                answer+='R'
                Rpos.append([targetx,targety])
            elif Lres==Rres:
                if hand=='right':
                    answer+='R'
                    Rpos.append([targetx,targety])
                elif hand=='left':
                    answer+='L'
                    Lpos.append([targetx,targety])


    return answer




inputs = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand="left"

answer = solution(inputs,hand)
print(answer)
