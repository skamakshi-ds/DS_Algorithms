def binarySearch(nums, target):
    left  = 0
    right = len(nums) - 1
    mid = 0
    while left < right:
        mid = (left + right)//2

        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target :
            left = mid + 1
        else :
            return mid

    return -1

if __name__ == "__main__":
    nums = [1,4,6,7,8,9,10]
    k = 9

    print(binarySearch(nums, k))

