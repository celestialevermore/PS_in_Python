N,M,K = map(int,input().split())


dx=[1,0,-1,0]
dy=[0,1,0,-1]





mapp = [['.']*M for _ in range(N)]



for i in range(K):
    a,b = map(int,input().split())
    mapp[a-1][b-1]='#'

visited=[]
index=-1
cntlist=[1]*1000

# for i in range(N):
#     for ii in range(M):
#         print(mapp[i][ii],end=' ')
#     print()


def DFS(visied,curcnt,x,y):

    for i in range(4):
        nx = x+dx[i] 
        ny = y+dy[i]

        if nx>=0 and nx<N and ny>=0 and ny<M and [nx,ny] not in visited and mapp[nx][ny]=='#':
            #print('next :',nx,ny)
            curcnt+=1
            visited.append([nx,ny])
            DFS(visited,curcnt,nx,ny)


    return curcnt




for i in range(N):
    for ii in range(M):
        if mapp[i][ii]=='#' and [i,ii] not in visited:
            #print('start at :',i,ii)
            visited.append([i,ii])
            index+=1
            cntlist[index]+=1
            #print('returned cnt :',DFS(visited,cntlist[index],i,ii))
            cntlist.append(DFS(visited,cntlist[index],i,ii))


print(max(cntlist))



