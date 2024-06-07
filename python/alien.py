def alientodecimal(code,language):
    n = len(code)
    m = len(language)
    list_ = {}
    for x in range(len(language)):
        list_[language[x]] = x
    sum = 0    
    for x in range(n-1,-1,-1):
        k = n-1-x
        sum += (list_[code[x]] * m**(k))
    return sum


def decimaltoalien(decimal,language):
    n = len(language)
    list_ = {}
    for x in range(len(language)):
        list_[x] = language[x]
    sum = ""
    while decimal != 0:
        sum = list_[decimal%n] + sum
        decimal = decimal//n
    return sum

t = int(input())
arr = []
for _ in range(t):
    temp = list(map(str,input().split()))
    arr.append(temp)
for x in range(len(arr)):
    decimal_ = alientodecimal(arr[x][0],arr[x][1])
    alien = decimaltoalien(decimal_,arr[x][2])
    print(f"Case #{+x+1}: {alien}")
    
    
