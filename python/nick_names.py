a = int(input())
names = [input() for _ in range(a)]
b = int(input())
nick_names = [input() for _ in range(b)]

list_ = []

for x in nick_names:
    count = 0
    for y in names:
        if(y.startswith(x)):
            count += 1
    list_.append(count)
    
for x in list_:
    print(x)
        
