"""
given a string, check if it is a permutation of a palindrome
ignore casing and non-letter characters
"""

"""
Initial thoughts
    eliminate pairs and passes if <= 1 character remains
        racecar -> aaccerr -> e (acceptable)
        racecarf -> aaccefrr -> ef (unacceptable)
    can we take advantage of the fact that we're only using lowercase letters, a-z?
        could use array of size 26 and store counts of ascii values
        correction to earlier thought, we don't care about eliminating pairs, we just need to check how many values in our array
            are odd. # odd values in array <= 1
        lowercase ASCII: 97-122
        ord(char) - 97
    can we do this without additional space?
        i don't think we can without greatly sacrificing time 
    does sorting help us? not really
    lowercase and strip whitespace
        unneccessary to eliminate whitespace, just skip them
"""

def palindrome_permutation(string):
    str_arr = list(string.lower())
    letter_counts = [0] * 26
    for letter in str_arr:
        ascii_val = ord(letter) - 97
        if ascii_val >= 0 and ascii_val <= 26:
            letter_counts[ascii_val] += 1
    
    num_odd = 0
    for val in letter_counts:
        num_odd += val % 2
    return num_odd <= 1

print(palindrome_permutation("tomcat"))
print(palindrome_permutation("race     CAr"))



"""
Learnings
1. mentioned in previous problem, but familiar self with common ASCII values/ranges, extended ASCII, Unicode
2. think of casing, whitespaces, special characters
    especially if a problem says to ignore casing, non-letters. may be able to take advantage of that
3. we could keep track of # of odd along the way. this may or may not even be faster though, but a consideration
4. bit vectors
"""