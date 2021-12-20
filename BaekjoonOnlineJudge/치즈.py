from sys import stdin 


N,M = map(int,input().split())
dx=[1,-1,0,0]
dy=[0,0,1,-1]

mapp = [list(map(int,stdin.readline().split())) for _ in range(N)]
res=[]
visited=[]
queue=[]
cnt=0


#아직 녹지 않은 치즈가 있는지를 검사하는 함수
def isone(mapp):
    for i in range(N):
        for ii in range(M):
            if mapp[i][ii]==1:
                return True
    return False 

#치즈의 숫자를 세는 함수
def count_of_cheeze(mapp):
    cnt=0
    for i in range(N):
        for ii in range(M):
            if mapp[i][ii]==1:
                cnt+=1
    return cnt 


def isair(mapp):
    for i in range(N):
        for ii in range(M):
            if mapp[i][ii]==0:
                visited.append([i,ii])


def BFS(mapp,visited,queue):

    while queue:
        curx,cury = queue[0][0],queue[0][1]
        del queue[0]

        #현재의 좌표에서 4방탐색을 하여 치즈가 공기에 접촉하였는지 여부를 판단.
        #만일 현재 좌표에서 4방탐색을 하였더니 0이 보이지 않는 밀폐된 곳이면 
        for i in range(4):
            nextx,nexty = curx+dx[i],cury+dy[i]
            if mapp[nextx][nexty]==0:
                mapp[curx][cury]=0
                break
            else:
                continue 
        


        for i in range(4):
            nextx,nexty = curx+dx[i],cury+dy[i]
            if mapp[nextx][nexty]==1 and nextx>=0 and nextx<N and nexty>=0 and nexty<M and [nextx,nexty] not in visited:



def search_one_and_BFS(mapp):
    for x in range(N):
        for y in range(M):
            if mapp[x][y]==1 and [x,y] not in visited:
                visited.append([x,y])
                queue.append([x,y])
                BFS(mapp,visited,queue)




while isone(mapp):
    cnt+=1

    search_one_and_BFS()


    res.append(count_of_cheeze(mapp))



