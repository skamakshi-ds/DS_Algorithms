
def palindrome(name):

    left  = 0
    right = len(name) - 1
    flagPalin = True
    while left < right:
        if name[left] == name[right]:
            left +=1
            right -=1
            if name[left] != name[right]:
                flagPalin = False
                break
        else:
            flagPalin = False
            break
    if flagPalin:
        print("Given name is Palin")
    else:
        print("Given name is not Palin")



if __name__ == "__main__":
    print("Hello World !!")
    palindrome("abccba")