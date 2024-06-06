n,c = tuple(map(int, input().split()))
numbers = list(map(int, input().split()))
mydict = {}
for x in numbers:
    if x in mydict:
        mydict[x] += 1
    else:
        mydict[x] = 1
list_ = sorted(mydict.items(), key=lambda x: x[1], reverse=True)
res = []
for x in list_:
    for i in range(mydict[x[0]]):
        res.append(x[0])
       
#join
print(' '.join(map(str, res)))
