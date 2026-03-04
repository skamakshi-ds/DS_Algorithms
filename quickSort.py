def quickSort(nums):
    temp =0

    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] < nums[j]:
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp

    print(nums)


def pop(nums) -> int:
    i = len(nums) - 1
    tempNum = 0
    if i >=0 :
        tempNum=nums[i]
        nums.remove(i)
    return tempNum

def push(nums,val):
    i = 0
    if len(nums) > 0:
        i = len(nums)-1
        nums[i+1] = val
    else:
        i = 0
        nums[i] = val


    return nums

def peek(nums):
    if len(nums) == 0:
        return -1
    else :
        return nums[len(nums)-1]



if __name__ == "__main__":
    nums = [2,3,7,6,5,1,10]
    quickSort(nums)
