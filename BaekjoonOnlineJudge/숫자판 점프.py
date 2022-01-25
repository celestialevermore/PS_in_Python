from sys import stdin 
from collections import deque 

dd = dict()

ss = set()

mapp = [list(stdin.readline().split()) for _ in range(5)]
visited = [[False]* 5 for _ in range(5)]

res = 0



dx = [0,0,1,-1]
dy = [1,-1,0,0]


def DFS(start,string):

    if len(string)==6:
        print('res :',string)
        if string not in ss:
            ss.add(string)

        if string not in dd:
            dd[string]=1
        else:
            dd[string]+=1
        return 
    else:
        for i in range(4):
            nx = start[0]+dx[i]
            ny = start[1]+dy[i]

            if nx>=0 and nx<5 and ny>=0 and ny<5:
                #visited[nx][ny]=True
                string+=mapp[nx][ny]
                next=[nx,ny]
                DFS(next,string)
                #visited[nx][ny]=False 
                string = string[0:len(string)]





for x in range(5):
    for y in range(5):
        string = ""
        string+=mapp[x][y]
        start = [x,y]
        #visited[x][y]=True
        print('start : ',x,y)
        DFS(start,string)
        #visited[x][y]=False




print(dd)

print()
print(ss)



