map_ = [list(map(int,input().split())) for _ in range(7)]

print()

for i in range(7):
    for ii in range(7):
        print(map_[i][ii], end=' ')
    print()
