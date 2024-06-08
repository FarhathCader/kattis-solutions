def bubble_sort(arr):
    for x in range(len(arr)-1):
        for y in range(len(arr)-x-1):
            if arr[y] > arr[y+1]:
                arr[y],arr[y+1] = arr[y+1],arr[y]



def bubble_sort_optimized(arr):
    for x in range(len(arr)-1):
        check = False
        for y in range(len(arr)-x-1):
            if arr[y] > arr[y+1]:
                arr[y],arr[y+1] = arr[y+1],arr[y]
                check = True
        if check == False:
            break



arr = list(map(int,input().split()))
bubble_sort(arr)
print(arr)

