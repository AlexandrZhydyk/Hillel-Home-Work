def max_depth(arr):
    depth = []
    for index in range(1, len(arr)-1):
        if arr[index] < arr[index-1] and arr[index] < arr[index+1]:
            depth.append(min(max(arr[:index+1]), max(arr[index:])) - arr[index])
    if depth:
        return max(depth)
    return 0

arr = [1, 2, 4, 5, 8, 4, 7, 5, 6, 0]
print(max_depth(arr))