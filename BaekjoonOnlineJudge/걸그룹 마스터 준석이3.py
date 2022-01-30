N,M = map(int,input().split())

group={}

for i in range(N):
    g_name = input() 
    member = int(input())

    for j in range(member):
        m_name=input()
        group[g_name]=group.get(g_name,[])+[m_name]


