def second_largest(arr):
    if len(arr) < 2:
        return None  # Not enough elements

    first = second = float('-inf')

    for num in arr:
        if num > first:
            second = first
            first = num
        elif first > num > second:  # num is between first and second
            second = num

    return second if second != float('-inf') else None

arr = [12, 10, 18, 34, 35, 35]
print("Second largest:", second_largest(arr))
