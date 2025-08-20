def rotateArr(arr, d):
    n = len(arr)   

    # If d is bigger than array size, take remainder
    d %= n

    # Step 1: Reverse first d elements
    reverse(arr, 0, d - 1)

    # Step 2: Reverse remaining (n-d) elements
    reverse(arr, d, n - 1)

    # Step 3: Reverse the whole array
    reverse(arr, 0, n - 1)


# Function to reverse part of an array
def reverse(arr, start, end):
    while start < end:
        # Swap elements at start and end
        arr[start], arr[end] = arr[end], arr[start]
        start += 1   # move start forward
        end -= 1     # move end backward

# Test the function
arr = [10, 20, 30, 40, 50, 60]
d = 3

print("Original array:", arr)
rotateArr(arr, d)
print(arr)
