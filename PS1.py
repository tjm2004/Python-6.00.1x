#Problem Set 1:

# Problem 1
# 10.0 points possible (graded)
# Assume s is a string of lower case characters.

# Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
# For example, if s = 'azcbobobegghakl', your program should print:
# Number of vowels: 5

count = []
vowels = ['a','e','i','o','u']
list_of_characters = list(s)

for character in list_of_characters:
    if character in vowels:
        count.append(character)
        
print('Number of vowels: ', len(count))

# Problem 2
# 10.0 points possible (graded)
# Assume s is a string of lower case characters.

# Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

# Number of times bob occurs is: 2

count = 0

for x in range(len(s) + 1 - len('bob')):
    if s[x:x+len('bob')] == 'bob':
        count = count + 1
        
print('Number of times bob occurs is: ', count)

# Problem 3
# 15.0/15.0 points (graded)
# Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

# Longest substring in alphabetical order is: abc
# Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, 
# we suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and cleared your head.

alphabet= {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,\
		   "i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,\
		   "p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,\
		   "w":22,"x":23,"y":24,"z":25}

start = 0
middle = 0
end = 1

bits = []
final_answer = ''


while middle != (len(s) - 1):
	if alphabet[s[start]] <= alphabet[s[end]]:   #SEARCH
		while len(s) != end and (alphabet[s[middle]] <= alphabet[s[end]]):
			middle += 1
			end += 1
		bits.append(s[start:end])# slice out section
		start = middle
	else:
		start += 1
		middle += 1
		end += 1

for bit in bits:
	if len(final_answer) < len(bit):
		final_answer = bit

if len(final_answer) == 0:
	final_answer = s[0]

print('Longest substring in alphabetical order is: '+final_answer)