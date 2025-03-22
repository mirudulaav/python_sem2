def rearrange_array(arr):
    n = len(arr)
    for i in range(1, n):
        if i % 2 == 1:
            if arr[i] >= arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
        else:
            if arr[i] <= arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
    return arr
arr = [5, 3, 1, 2, 3, 7, 6, 4]
output = rearrange_array(arr)
print("Output:", output)
