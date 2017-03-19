def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) == 0:
        return False
    if len(aStr) == 1 and aStr == char:
        if aStr ==char:
            return True
        else:
            return False
    if char == aStr[len(aStr)//2]:
        return True
    if len(aStr)>1:
        if char > aStr[len(aStr)//2]:
            new = aStr[len(aStr)//2:]
            return isIn(char, new)
        if char < aStr[len(aStr)//2]:
            new = aStr[:len(aStr)//2]
            return isIn(char, new)