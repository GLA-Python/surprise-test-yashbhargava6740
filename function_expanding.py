def expanding(arr :list):
    lst1 = []
    for i in range(len(arr)-1):
        lst1.append(abs(arr[i+1]-arr[i]))
    c = 0
    for i in range(len(lst1)-1):
        if lst1[i+1] > lst1[i]:
            c = 1
        else:
            c = 0
            break
    if c == 1:
        return True
    else:
        return False
inp = list(map(int,input().split()))
out = expanding(inp)
print(out)