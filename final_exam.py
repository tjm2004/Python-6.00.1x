trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}

def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    num = int(us_num)
    if num < 11:
        return trans[str(num)]
    elif num < 20:
        return ('shi ' + trans[str(num - 10)])
    else:
        first = trans[us_num[0]]
        if num%10 == 0:
            return (first + ' shi')
        else:
            last = trans[us_num[1]]
            return (first + ' ' + 'shi ' + last)

###############################################################################

def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    cases = {}
    min_value = 0
    i,j = 0,1

    def inc(i,j):
        k = i
        while (j < len(L)-1) and (L[k+1] <= L[j+1]):
            k = j
            j += 1
        cases[i] = len(L[i:j+1])
        i,j = check(j-1,j)
        i,j = j,j+1
        return [i,j]

    def dec(i,j):
        k = i
        while (j < len(L)-1) and L[k+1] >= L[j+1]:
            k = j
            j += 1
        cases[i] = len(L[i:j+1])
        if i != 0:
            i,j = check(j-1,j)
        i,j = j,j+1
        return [i,j]

    def same(i,z):
        cases[i] = len(L[i:z+1])
        i,j = z, z+1
        return [i,j]

    def check(i,j):
        if L[i] == L[j]:
            while i >= 1:
                return check(i-1, j-1)
        else:
            return [i,j]
   
    while j < len(L):
        z = j
        while L[i] == L[z] and (z < len(L)-1):
            z += 1
        if L[i] < L[z]:
            i,j = inc(i,j)
        elif L[i] > L[z]:
            i,j = dec(i,j)
        else:
            i,j = same(i,z)
        
    for pos, val in cases.items():
        if val > min_value:
            min_value = val
            answer = pos

    return sum(L[answer:answer+min_value])

###############################################################################################################

## DO NOT MODIFY THE IMPLEMENTATION OF THE Person CLASS ##
class Person(object):
    def __init__(self, name):
        #create a person with name name
        self.name = name
        try:
            firstBlank = name.rindex(' ')
            self.lastName = name[firstBlank+1:]
        except:
            self.lastName = name
        self.age = None
    def getLastName(self):
        #return self's last name
        return self.lastName
    def setAge(self, age):
        #assumes age is an int greater than 0
        #sets self's age to age (in years)
        self.age = age
    def getAge(self):
        #assumes that self's age has been set
        #returns self's current age in years
        if self.age == None:
            raise ValueError
        return self.age
    def __lt__(self, other):
        #return True if self's name is lexicographically less
        #than other's name, and False otherwise
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    def __str__(self):
        #return self's name
        return self.name
        
class USResident(Person):
    """ 
    A Person who resides in the US.
    """
    def __init__(self, name, status):
        """ 
        Initializes a Person object. A USResident object inherits 
        from Person and has one additional attribute:
        status: a string, one of "citizen", "legal_resident", "illegal_resident"
        Raises a ValueError if status is not one of those 3 strings
        """
        Person.__init__(self, name)
        if status in ['citizen', 'legal_resident', 'illegal_resident']:
            self.status = status
        else:
            raise ValueError("USResident must have correct status")

        
    def getStatus(self):
        """
        Returns the status
        """
        return self.status

##############################################################################################

class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer): 
    def __init__(self, name):
        Lecturer.__init__(self, name)
        self.title = 'Prof. '
    def say(self, stuff): 
        return self.title + self.name + ' says: ' + self.lecture(stuff)

class Professor(Lecturer): 
    def say(self, stuff): 
        return self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor): 
    def say(self, stuff): 
        return self.name + ' says: ' + 'It is obvious that ' + Lecturer.lecture(self, stuff)
    def lecture(self, stuff):
        return 'It is obvious that ' + Lecturer.lecture(self, stuff)


e = Person('eric') 
le = Lecturer('eric') 
pe = Professor('eric') 
ae = ArrogantProfessor('eric')

assert e.say('the sky is blue') == 'eric says: the sky is blue'
assert le.say('the sky is blue') == 'eric says: the sky is blue'
assert le.lecture('the sky is blue') == 'I believe that eric says: the sky is blue'
assert pe.say('the sky is blue') == 'eric says: I believe that eric says: the sky is blue'
assert pe.lecture('the sky is blue') == 'I believe that eric says: the sky is blue'
#assert ae.say('the sky is blue') == 'eric says: It is obvious that eric says: the sky is blue'
assert ae.say('the sky is blue') == 'eric says: It is obvious that I believe that eric says: the sky is blue'
#assert ae.lecture('the sky is blue') == 'It is obvious that eric says: the sky is blue'
assert ae.lecture('the sky is blue') =='It is obvious that I believe that eric says: the sky is blue'


###############################################################################################################

def general_poly(L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
	k = list(range(len(L)))[::-1]
	def answer(x):
		ans = 0
		pos = 0
		for value in L:
			ans += value * x ** k[pos]
			pos += 1
		return ans
	return answer