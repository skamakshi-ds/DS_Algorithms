def checkIfPangram(sentence):
    newSet = set()

    for testChar in sentence:

        if testChar not in newSet:
            newSet.add(testChar)
        else:
            print(testChar)
            return False

    return True

def missingNumber(nums):
    n = len(nums)

    expected_Sum = n * (n+1) // 2
    actual_sum = sum(nums)
    missing_number = expected_Sum - actual_sum
    print(missing_number)

def bruteSet_missNum(nums):

    n = len(nums)
    missing_num = set()
    for i in range(n):
        if i not in nums :
            missing_num.add(i)

    print(missing_num)

def bruteHash_atleastKelement(nums, k):
    print(f"Pre : {nums}")
    count = 0
    newHash = {}
    newSet = set(nums)

    for i in nums:
        if count != k and i not in newHash :
            newHash[i] = 1
            count += 1
        else:
            newHash[i] += 1

        if count == len(newHash) == k:
            return newHash.keys()

    return None


if __name__ == "__main__":
    print(checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))

    nums = [1,3,5,6,9,10,2]
    bruteSet_missNum(nums)
    Snums = "aabaecc"
    print(bruteHash_atleastKelement(Snums, 2))


