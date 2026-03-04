#given an integer array nums and target k, try to find the longest subarray whose sum is less than or equal to k.
from typing import List


def func_longSubA(nums, k) -> int:
    left = 0
    right  = 0
    newArray = [0] * 2
    newSum = 0
    ans =0

    for right in range (len(nums)):
        newSum += nums[right]

        while newSum > k:
            newSum -= nums[left]
            left += 1

        print(f"right : {right}")
        print(f"left: {left}")
        ans = max (ans, right-left+1)
    return ans


def twoIndices(nums, k) -> list[int] | None:

    newArray = []
    for i in range (len(nums)):
        for j in range (1, len(nums)):
            newSum = nums[i] + nums[j]
            if newSum != k:
                continue
            elif newSum == k:
                newArray.append(i)
                newArray.append(j)
                return newArray


# def twoIndices_hashMap(nums, k):
#
#     hashDict = {}
#     newArray = []
#     for i in range (len(nums)):
#         num = k-nums[i]
#
#         if hashDict is not None and i in hashDict:

def twoSum(nums: List[int], target: int) -> List[int]:
    dic = {}
    for i in range(len(nums)):
        num = nums[i]
        complement = target - num
        print(f"t: {target}")
        print(f"num : {num}")
        print(f"comple : {complement}")

        if complement in dic:  # This operation is O(1)!
            return [i, dic[complement]]

        dic[num] = i

    return [-1, -1]

def brute_firstChar(strTest) :

    print(strTest)
    dictTest = {}
    for i in strTest :
        if i in dictTest :
            return i

        dictTest[i] = i

    return None

def brute_xAvail(nums):
    print(f"Pre : {nums}")
    xAvailSet = set(nums)
    newList = []
    for num in xAvailSet :
        print(num+1)
        xAdd = num + 1
        xSub = num - 1

        if (xAdd not in xAvailSet) and (xSub not in xAvailSet):
            newList.append(num)
    print(newList)


if __name__ == "__main__":
    nums = [11,13,54,55,67,68]
    k = 101

    # print(f"Value :{func_longSubA(nums, k)}")

    #arrayVal = twoIndices(nums, k)
    arrayVal = twoSum(nums,k)
    if arrayVal is not None and len(arrayVal) > 1:
        print(arrayVal[0])
        print(arrayVal[1])

    dict_Val = {1: "hello", 2: "giant", 3: "work", 4: "situation"}
    complement = "giant"
    if complement in dict_Val:
        print("Giant Exist")
    else:
        print("giant doesn't exist")
    strTest = "Ggiiaantt"
    print(f"First Char : {brute_firstChar(strTest)}")

    brute_xAvail(nums)

