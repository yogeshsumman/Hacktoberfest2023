def find_peak_infinite_array(arr):
    left, right = 0, 1  # Initialize the search range

    # Expand the search range exponentially until a peak is found
    while arr[right] > arr[left]:
        left = right
        right *= 2

    # Once the search range is established, perform binary search
    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return arr[mid]  # Found a peak element
        elif arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # No peak element found

# Example usage
infinite_array = [1, 3, 20, 4, 1, 0]
peak = find_peak_infinite_array(infinite_array)
if peak != -1:
    print("Peak element in the infinite array:", peak)
else:
    print("No peak element found in the infinite array.")
