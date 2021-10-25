start = [list(map(int,input().split())) for _ in range(7)]


def check(cur):

    if cur[0] == cur[4] and cur[1] == cur[3]:
        return True
    else:
        return False 

rescnt=0


for i in range(7):

    for startpoint in range(3):
        #startpoint가 0일때 즉 map[0][0]일 때 ~ map[0][2]까지
        cur1 = [start[i][startpoint],start[i][startpoint+1],start[i][startpoint+2],start[i][startpoint+3],start[i][startpoint+4]]
        cur2 = [start[startpoint][i],start[startpoint+1][i],start[startpoint+2][i],start[startpoint+3][i],start[startpoint+4][i]]
        
        if check(cur1):
            rescnt+=1
        if check(cur2):
            rescnt+=1


print(rescnt)


