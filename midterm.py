#MIDTERM

# Problem 4
# 10.0/10.0 points (graded)
# Implement a function called closest_power that meets the specifications below.

# def closest_power(base, num):
#     '''
#     base: base of the exponential, integer > 1
#     num: number you want to be closest to, integer > 0
#     Find the integer exponent such that base**exponent is closest to num.
#     Note that the base**exponent may be either greater or smaller than num.
#     In case of a tie, return the smaller value.
#     Returns the exponent.
#     '''
#     # Your code here
# For example,

# closest_power(3,12) returns 2
# closest_power(4,12) returns 2
# closest_power(4,1) returns 0

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    low = 0
    high = 1
    if base**low == num:
        return low
    while True:
        if base**low <= num <= base**high:
            a = (num - base**low)
            b = (base**high - num)
            if min(a,b) == a:
                return low
            else:
                return high
        else:
            low +=1
            high +=1

# Problem 5
# 10.0/10.0 points (graded)
# Write a Python function that returns the sum of the pairwise products of listA and listB. You should assume that listA and listB have the same length and are two lists of integer numbers. For example, if listA = [1, 2, 3] and listB = [4, 5, 6], the dot product is 1*4 + 2*5 + 3*6, meaning your function should return: 32

# Hint: You will need to traverse both lists in parallel.

# This function takes in two lists of numbers and returns a number.

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    if len(listA) == 1:
        return listA.pop(0)*listB.pop(0)
    else:
        return (listA.pop(0)*listB.pop(0)) + dotProduct(listA, listB)


# Problem 6
# 15.0/15.0 points (graded)
# Implement a function that meets the specifications below.
# For example, if L = [[1, 2], [3, 4], [5, 6, 7]] then deep_reverse(L) mutates L to be [[7, 6, 5], [4, 3], [2, 1]]

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    for x in L:
        x.reverse()
    L = L.reverse()

# Problem 7
# 20.0/20.0 points (graded)
# Assume you are given two dictionaries d1 and d2, each with integer keys and integer values. You are also given a function f, that takes in two integers, performs an unknown operation on them, and returns a value.

# Write a function called dict_interdiff that takes in two dictionaries (d1 and d2). The function will return a tuple of two dictionaries: a dictionary of the intersect of d1 and d2 and a dictionary of the difference of d1 and d2, calculated as follows:

# intersect: The keys to the intersect dictionary are keys that are common in both d1 and d2. To get the values of the intersect dictionary, look at the common keys in d1 and d2 and apply the function f to these keys' values -- the value of the common key in d1 is the first parameter to the function and the value of the common key in d2 is the second parameter to the function. Do not implement f inside your dict_interdiff code -- assume it is defined outside.
# difference: a key-value pair in the difference dictionary is (a) every key-value pair in d1 whose key appears only in d1 and not in d2 and (b) every key-value pair in d2 whose key appears only in d2 and not in d1.
# Here are two examples:

# If f(a, b) returns a + b
# d1 = {1:30, 2:20, 3:30, 5:80}
# d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
# then dict_interdiff(d1, d2) returns ({1: 70, 2: 70, 3: 90}, {4: 70, 5: 80, 6: 90})
# If f(a, b) returns a > b
# d1 = {1:30, 2:20, 3:30}
# d2 = {1:40, 2:50, 3:60}
# then dict_interdiff(d1, d2) returns ({1: False, 2: False, 3: False}, {})

def dict_interdiff(d1,d2):
    intersect = {}
    difference = {}
    for x in d1:
        if x in d2:
            intersect[x] = f(d1.get(x), d2.get(x))
    for x in d1:
        if x not in d2:
            difference[x] = d1.get(x)
    for x in d2:
        if x not in d1:
            difference[x] = d2.get(x)
    return (intersect,difference)


# Problem 8
# 20.0/20.0 points (graded)
# Implement a function that meets the specifications below.

# def applyF_filterG(L, f, g):
#    """
#     Assumes L is a list of integers
#     Assume functions f and g are defined for you. 
#     f takes in an integer, applies a function, returns another integer 
#     g takes in an integer, applies a Boolean function, 
#         returns either True or False
#     Mutates L such that, for each element i originally in L, L contains  
#         i if g(f(i)) returns True, and no other elements
#     Returns the largest element in the mutated L or -1 if the list is empty
#    """
#     # Your code here
# For example, the following functions, f, g, and test code:

# def f(i):
#     return i + 2
# def g(i):
#     return i > 5

# L = [0, -10, 5, 6, -4]
# print(applyF_filterG(L, f, g))
# print(L)
# Should print:

# 6
# [5, 6]

def applyF_filterG(L,f,g):
    for x in L[:]:
        if g(f(x)) != True:
            L.remove(x)
    if len(L) == 0:
        return -1
    else:
        return max(L)

# Problem 9
# 15.0/15.0 points (graded)
# Write a function to flatten a list. The list contains other lists, strings, or ints. For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5] is flattened into [1,'a','cat',2,3,'dog',4,5] (order matters).

# def flatten(aList):
#     ''' 
#     aList: a list 
#     Returns a copy of aList, which is a flattened version of aList 
#     '''
  

# Click to expand Hint: How to think about this problem
# Recursion is extremely useful for this question. You will have to try to flatten every element of the original list. To check whether an element can be flattened, the element must be another object of type list.

# Paste your entire function, including the definition, in the box below. Do not leave any debugging print statements. Note that we ask you to write a function only -- you cannot rely on any variables defined outside your function for your code to work correctly.


def flatten(aList):
    for x in aList[:]:
        if x.__class__.__name__ == 'list':
            index = aList.index(x)
            aList.remove(x)
            for x in flatten(x)[::-1]:
                aList.insert(index, x)
    return aList