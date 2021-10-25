
sutoku = [list(map(int,input().split())) for _ in range(9)]


for i in range(9):
    for j in range(9):
        print(sutoku[i][j], end=' ')
    print()

print()



flag=0

for i in range(1,10):