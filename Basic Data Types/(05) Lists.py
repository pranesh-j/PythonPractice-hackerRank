N = int(input())
arr = []
while N > 0:
    opn = list(map(str,input().split()))
    if opn[0] == "insert":
        arr.insert(int(opn[1]),int(opn[2]))
    if opn[0] == "print":
        print(arr)
    elif opn[0] == "remove":
        arr.remove(int(opn[1]))
    elif opn[0] == "append":
        arr.append(int(opn[1]))
    elif opn[0] == "sort":
        arr.sort()
    elif opn[0] == "pop":
        arr.pop()
    elif opn[0] == "reverse":
        arr.reverse()
    N -= 1
