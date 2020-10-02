a = input()

inputs = a.split(",")

def reverseList(x):
    for i in range(len(x)-1,-1,-1):
        print(x[i],end=" ")

reverseList(inputs)