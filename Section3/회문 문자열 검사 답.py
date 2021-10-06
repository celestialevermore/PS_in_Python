n = int(input())

for i in range(n):
    s = input()

    s=s.upper()
    #와.................................
    size = len(s)
    for j in range(size//2):
        if s[j]!=s[-1-j]:
            print("#%d NO" %(i+1))
    else:
        print("#%d YES" %(i+1))
