def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:  # jbtk left chota h tbtk swap krna h
     
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr

# Example
arr = [1, 2, 3, 4, 5]
print(reverse_array(arr))  # [5, 4, 3, 2, 1]