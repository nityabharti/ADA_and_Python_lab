"""
Implement Binary Search
"""
def binary_search(arr: list, target, low=0, high=None) -> int:
    len_arr = len(arr)
    if high is None:
        high = len_arr
    mid = low+((high-low)//2)
    if high < low:
        return -1
    if target == arr[mid]:
        return mid
    if target > arr[mid]:
        return binary_search(arr, target, mid+1, len_arr)
    else:
        return binary_search(arr, target, low, mid-1)


if __name__ == '__main__':
    print("Enter comma seperated values for array of values: ")
    values = input().split(',')

    values = list(map(int, values))
    print("Array:", values)

    target = int(input("Enter target value: "))

    idx = binary_search(values, target, 0, len(values))

    if idx == -1:
        print("Target not found")
    else:
        print(f'Target found at index {idx}')