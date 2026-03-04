# Given an array arr[] of size n, find the element that appears more than ⌊n/2⌋ times.
# If no such element exists, return -1.
#
# Examples:
#
# Input: arr[] = [1, 1, 2, 1, 3, 5, 1]
# Output: 1
# Explanation: Element 1 appears 4 times. Since ⌊7/2⌋ = 3, and 4 > 3, it is the majority element.
#
# Input: arr[] = [7]
# Output: 7
# Explanation: Element 7 appears once. Since ⌊1/2⌋ = 0, and 1 > 0, it is the majority element.
#
# Input: arr[] = [2, 13]
# Output: -1
# Explanation: No element appears more than ⌊2/2⌋ = 1 time, so there is no majority element.


def findMultipleElement(nums) :
    value  = len(nums) // 2

    test_dict = {}
    for n in nums :
        if n in test_dict:
            test_dict[n] +=1
        elif n not in test_dict:
            test_dict[n] = 1

    print(test_dict)
    print(value)

    answArray = []
    for k in test_dict.keys():
        if test_dict[k] >= value:
            answArray.append(k)

    if len(answArray)  == 0:
        return -1
    else :
        return answArray


# Given an array of words arr[], the task is to groups strings that are anagrams.
# An anagram is a word or phrase formed by rearranging the letters of another,
# using all the original letters exactly once.
#
# Example:
#
# Input: arr[] = ["act", "god", "cat", "dog", "tac"]
# Output: [["act", "cat", "tac"], ["god", "dog"]]
# Explanation: There are 2 groups of anagrams "god", "dog" make group 1. "act", "cat", "tac" make group 2.
#
# Input: arr[] = ["listen", "silent", "enlist", "abc", "cab", "bac", "rat", "tar", "art"]
# Output: [["abc", "cab", "bac"], ["listen", "silent", "enlist"],["rat", "tar", "art"]]
# Explanation:
# Group 1: "abc", "bac" and "cab" are anagrams.
# Group 2: "listen", "silent" and "enlist" are anagrams.
# Group 3: "rat", "tar" and "art" are anagrams.

def groupAnagram(arr):

    newDict = {}
    for val in arr:
        newDict[val] = getSum(val)

    grouped_by_value = {}

    for key,value in newDict.items():
        grouped_by_value.setdefault(value, []).append(key)


    print(grouped_by_value)
    return grouped_by_value


def getSum(strVal) -> int:
    add = 0
    for char in strVal :
        add += ord(char)

    return add


def getStockSpan(nums):

    left = 0
    span = []
    span.append(1)
    right  = 1
    flag = True
    while right < len(nums) and left < right: # get the left and right value
        count = 1
        for item in range(0, right+1):
            if nums[right] < nums[right-1]: # check first the element and previous element if it is small just make span 1 and exit
                span.append(1)
                break
            elif nums[right] > nums[item]: # if above condition doesn't meet, then check all the items in the row which are small and keep counting the span which ever is small and keep adding.
                count  += 1
                flag  = False

        if not flag :
            span.append(count)

        right +=1
        flag = True


    print(span)


def depthFirst(grid,x,y,oldVal, newVal):
    m = len(grid)
    n = len(grid[0])
    if x < 0 or x >= m or y < 0 or y >=n:
        return

    if grid[x][y] != oldVal:
        return

    # replace Value :
    grid[x][y] = newVal

    depthFirst(grid, x, y+1, oldVal, newVal)
    depthFirst(grid, x, y-1, oldVal, newVal)
    depthFirst(grid, x+1, y, oldVal, newVal)
    depthFirst(grid, x-1, y, oldVal, newVal)


def fill(grid):
    m = len(grid)
    n = len(grid[0])

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'O':
                grid[i][j] = '-'

    print(grid)

    # all the Edge to be filled with O instead of - and
    # its consecutive sides which are in contact

    for i in range(n):
        if grid[i][0] == '-':
            depthFirst(grid, i, 0, '-','O')
        if grid[i][n-1] == '-':
             depthFirst(grid,i, n-1, '-','O')

    for j in range(m):
        if grid[0][j] == '-':
            depthFirst(grid,0, j, '-','O')
        if grid[m-1][j] == '-':
            depthFirst(grid, m-1, j, '-','O')

    print(grid)

    #Replace remaining '-' with 'x'
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '-':
                grid[i][j] = 'X'

    print(grid)





if __name__ == "__main__":
    nums = [1,3,2,7,2,1,3,2,7,1]

    print(findMultipleElement(nums))
    arr = ["act", "god", "cat", "dog", "tac"]

    print(groupAnagram(arr))

    getStockSpan([10, 4, 5, 90, 120, 80])

    grid = [['X', 'O', 'X', 'X', 'X', 'X'],
                ['X', 'O', 'X', 'X', 'O', 'X'],
                ['X', 'X', 'X', 'O', 'O', 'X'],
                ['O', 'X', 'X', 'X', 'X', 'X'],
                ['X', 'X', 'O', 'X', 'X', 'O'],
                ['O', 'O', 'X', 'O', 'O', 'O']]

    fill(grid)