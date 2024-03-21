import random

def naive_search (l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

def binary_search (l, target, low=None, high=None):
    if low == None: 
        low = 0
    if high == None:
        high = len(l) - 1
    if low > high:
        return -1 
    
    # example l= [1, 3, 10, 12, 14]
    mid_point = (low + high) // 2

    if l[mid_point] == target:
        return mid_point
    
    elif l[mid_point] < target:
        return binary_search(l, target, mid_point+1, high)
    
    # l[mid_point] > target:
    else:
        return binary_search(l, target, low, mid_point-1)

# l = [1, 3, 10, 12, 14]
# target = 14
# result = binary_search(l, target)
# print(result)


length = 1000
sorted_list = set()
while len(sorted_list) < length:
    sorted_list.add(random.randint(-4*length, 4*length))  
sorted_list = sorted(list(sorted_list))
target =  1000


result = binary_search(sorted_list, target)
print(result)

