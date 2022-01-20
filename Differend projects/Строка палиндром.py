def isPalindrome(NumberAsString):
    
    chars = list(NumberAsString)
    IsPalindrome = True

    for index in range(len(chars) // 2):
        element = chars[index]

        if element != chars[len(chars) - 1 - index]:
            IsPalindrome = False
            break

    return IsPalindrome


# Test cases
print(isPalindrome("101"))
print(isPalindrome("1001"))
print(isPalindrome('12345'))
print(isPalindrome('123321'))