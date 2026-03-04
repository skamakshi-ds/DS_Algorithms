def getMaxWater(nums):
    n = len(nums)

    left =1
    right =len(nums)-2

    lmax = nums[left-1]
    rmax = nums[right+1]
    res = 0

    while left <= right :

        if rmax <= lmax :
            res += max(0,rmax - nums[right])
            rmax = max(rmax, nums[right])
            right -=1
        else:
            res += max(0,lmax - nums[left])
            lmax = max(lmax, nums[left])
            left  +=1

    return res

def getTwoSortedArray(num1, num2):

    # num1 = [1,4,6,9]
    # num2 = [5,7,9,10,11]
    newArr = []
    m = len(num1)
    n = len(num2)
    i , j = 0 , 0
    while i < m and j < n :

        if num1[i] <= num2[j]:
            newArr.append(num1[i])
            i +=1

        else:
            newArr.append(num2[j])
            j +=1


    while i < n :
        newArr.append(num1[i])
        i+=1

    while j < n :
        newArr.append(num2[j])
        j +=1

    arr1 = []
    arr2 = []

    for i in range(m):
        arr1.append(newArr[i])

    for i in range(n):
        arr2.append(newArr[i])

    return arr1, arr2

def histogram(nums):
    n = len(nums)
    curr= 0
    res = 0
    for i in range(n):
        j = i -1
        while j >=0 and nums[j] >= nums[i]:
            curr += nums[i]
            j -=1

        j = i+1
        while j < n and nums[j] >= nums[i]:
            curr +=nums[i]
            j +=1



def longestConsecutive(nums):

    nums.sort()
    val = nums[0]
    count = 1
    res = 1
    for i in range(1,len(nums)):
        if nums[i-1] == nums[i]:
            continue

        else:
            if nums[i] == nums[i-1] + 1:
                count +=1
            else:
                count = 1
        res = max(res, count)

    return res

#
def countDistinct(nums, k):
   left  = 0
   right = len(nums)
   newArray = []
   count = 0
   i = 0
   newString = ""
   newMap = {}
   while left < right :
       for i in range(left, right):
           if nums[i] not in newString and len(newString) != k:
               newString += nums[i]
           else :
               if len(newString) != 0 :
                   newMap[newString] = len(newString)
                   if len(newString) == k:
                       print(newString)
                       count +=1
               newString = ""
               left +=1
               break

   # count=0
   # for item in newMap.keys():
   #     if newMap[item] == k:
   #        count +=1

   return count




if __name__ == "__main__":
    arr = [2, 1, 5, 3, 1, 0, 4]
    print(getMaxWater(arr))
    print(histogram([60, 20, 50, 40, 10, 50, 60]))
    print(countDistinct("aa",1))