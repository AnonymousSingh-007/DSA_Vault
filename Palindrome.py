#brute force appraoch
def isPalindrome(self, x: int) -> bool:
    xstr = str(x)
    return xstr == xstr[::-1]



