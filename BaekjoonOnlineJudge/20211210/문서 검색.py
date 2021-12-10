
inputs = input() 

start=input()
rescnt=0
index=-1
while True:
    index = inputs.find(start,index+1)
    if index==-1:
        break
    else:
        rescnt+=1

print(rescnt)

