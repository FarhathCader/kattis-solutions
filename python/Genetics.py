def difference(a,b):
    diff = 0
    print(a,b)
    for x in range(len(a)):
        if a[x] != b[x]:
            diff += 1
    print(diff)
    return diff

n,m,k = tuple(map(int,input().split()))
arr = []
for _ in range(n):
    k = list(input())
    arr.append(k)

for x in range(n):
    check = False
    for y in range(x+1,n):
        # print(arr[x],arr[y])
        if difference(arr[x],arr[y]) != k:
            check = True
            continue
    if check == False:
        print(x+1)
        break

            




