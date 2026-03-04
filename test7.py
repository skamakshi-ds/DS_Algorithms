# find the equilibrium between array
# function (array(val)) returns in such a way that func(array(1)) = function(array(2))

def function(x: list[int]) -> int:

    if len(x) == 1:
        return 0

    else:
        flag = 0
        for index in range(1,len(x)):
            left = 0
            right = len(x) - 1
            print(f"index : {index}")
            firstIteration = 0
            while left != index:
                firstIteration = firstIteration + x[left]
                left +=1
            secondIteration = 0
            while right != index:
                secondIteration = secondIteration + x[right]
                right -=1

            if firstIteration == secondIteration :
                return index
            else:
                continue


if __name__ == "__main__":
    x = [-7, 1, 5, 2, -4, 3, 0]
    print(f"Is Equilibrium :  {function(x)} ")