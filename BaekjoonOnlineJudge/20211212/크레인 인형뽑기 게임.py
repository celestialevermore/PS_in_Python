def solution(board,moves):
    answer=0

    bin=[0]
    
    for i in range(len(moves)):
        crainposition = moves[i]-1
        
        flag=0 #상단이 비었는지 비지 않았는지 검사 하기 위한 flag
        doll=0 #만일 비어있지 않을 경우 바구니에 넘기기 위한 복사 원소 

        #검사 시작
        for ii in range(len(board[crainposition])):
            #뭔가 0이 ㅇ아닌 어떤 것이 발견!
            if board[ii][crainposition]!=0:
                flag=1
                doll = board[ii][crainposition]
                #인형을 집었으니 해당 좌표는 0으로 만들어준다.
                board[ii][crainposition]=0
                break 

        #만일 flag가 1이라면 doll을 바구니에 넘겨준다.
        #만일 flag가 0이라면 다음으로 넘어가면 된다. 

        #인형을 집을 수 없었던 경우
        if flag==0:
            continue
        
        #인형을 제대로 집어낸 경우
        elif flag==1:

            if bin[-1]==doll:
                bin.pop()
                answer+=2
            else:
                bin.append(doll)

    return answer 




board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves=[1,5,3,5,1,2,1,4]

answer = solution(board,moves)
print(answer)