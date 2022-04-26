def binary(nums: list, target: int) -> int:
    low = 0
    up = len(nums) - 1
    while low <= up:
        mid = low + (up - low) //2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            up = mid - 1
        else:
            low = mid + 1
    return -1

if __name__ == '__main__':
    a = [8, 3, 5, 0, 49, 20, 84, 2, 12, 54, 13, 51, 67, 89]
    print(binary(a, 4))
    print(binary(a, 5))
    