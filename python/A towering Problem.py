

list_ = list(map(int,input().split()))
tower_sizes = list_[6:]
list_.pop()
list_.pop()
list_.sort(reverse= True)

stack1 = [list_[0]]
stack2 = []
i,j = 0,0
for x in range(1,len(list_)):
    for y in range(x+1,len(list_)):
        # print(list_[x],list_[y],stack1[0],tower_sizes)
        if list_[x] + list_[y] + stack1[0] in tower_sizes:
            stack1.append(list_[x])
            stack1.append(list_[y])
            i,j = x,y
            break
    if i != 0:
        break
for x in range(1,len(list_)):
    if x != i and x != j:
        stack2.append(list_[x])

print(*stack1,sep=" ",end=" ")
print(*stack2,sep=" ")
