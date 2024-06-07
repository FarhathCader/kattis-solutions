import math
def best_score(arr, n):
    if len(arr) == 0:
        return 0
    arr.sort(reverse=True)
    return sum(arr[:min(n, len(arr))])
import random
def required_points(arr, n):
    if(arr == []):
        return []
    return [n - best_score(i, 3) for i in arr]

def check(stack1, stack2, max_stack1, sum_stack2):
    global count
    # print(stack1, stack2,max_stack1, math.ceil(sum_stack2 / len(stack2)))
    if(len(stack1) != len(stack2)):
        print(1/0)
    if stack1 and max_stack1 <= (math.ceil (sum_stack2 / len(stack2))):
        count += len(stack1)
        stack1.clear()
        stack2.clear()
        return 0, 0  # Return updated max_stack1 and sum_stack2 as 0 since stacks are cleared
    return max_stack1, sum_stack2  # Return the original values if no clearing happens
count = 0
contests, users = map(int, input().split())


all_scores = []
my_best_score = best_score(list(map(int, input().split())), 4)
for _ in range(users - 1):
    scores = list(map(int, input().split()))
    other_best_score = best_score(scores, 4)
    if other_best_score > my_best_score:
        count += 1
    else:
        all_scores.append(scores)
        
        
arr = required_points(all_scores, my_best_score)
arr.sort()
n = len(arr)
points = [100, 75, 60, 50, 45, 40, 36, 32, 29, 26, 24, 22, 20, 18, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

if n > 30:
    points = points[:30] + [1] * (n - 30)
else:
    points = points[:n]
points.sort()

stack1 = []
stack2 = []
max_stack1 = 0
sum_stack2 = 0

if(len(arr) != len(points)):
    print(1/0)

# print(arr, points)

for i in range(n):
    if arr[i] <= (points[i]) and not stack1:
        count += 1
    else:
        stack1.append(arr[i])
        stack2.append(points[i])
        max_stack1 = max(max_stack1, arr[i])  # Update max_stack1
        sum_stack2 += points[i]  # Update sum_stack2
        max_stack1, sum_stack2 = check(stack1, stack2, max_stack1, sum_stack2)
stack2.reverse()
while stack1:
    max_stack1 = stack1[-1]
    max_stack1, sum_stack2 = check(stack1, stack2, max_stack1, sum_stack2)
    if stack1:
        sum_stack2 -= stack2.pop()
        stack1.pop()
        
        
        
    else:
        break

print(count + 1)