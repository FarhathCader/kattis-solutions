def difference(a,b):
    diff = 0
    print(a,b)
    diff += abs(a.count('A') - b.count('A'))
    diff += abs(a.count('T') - b.count('T'))
    diff += abs(a.count('G') - b.count('G'))
    diff += abs(a.count('C') - b.count('C'))
    print("diff",diff)
    return diff

n,m,k = tuple(map(int,input().split()))
list_ = [[None for _ in range(n)] for _ in range(n)]
arr = []
for _ in range(n):
    temp = list(input())
    arr.append(temp)

for x in range(n):
    for y in range(x,n):
        # print(arr[x],arr[y])
        if(x == y):
            list_[x][y] = k
        else:
            list_[x][y] = difference(arr[x],arr[y])
            list_[y][x] = list_[x][y]
        # print(list_[x][y])
print(list_)
for x in range(n):   
    if(len(set(list_[x])) == 1):
        print(list_[x][0])
        exit()

            




