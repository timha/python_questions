"""
replace all spaces in a string with '%20'
assume the string has sufficient space at the end to hold the additional characters
"""

"""
Initial thoughts
    one whitespace seems simple, what if there are 2+ spaces in a row?
        how do we keep track of all the characters that are being replaced?
        could use temp array but defeats the purpose of doing it in place
        going from end -> start resolves that problem
    assume input string is a character array since strings are immutable in python
"""


def URLify(string, length):
    overwrite_index = len(string)
    for i in range(length - 1, -1, -1):
        if string[i] == ' ':
            string[overwrite_index - 3:overwrite_index] = ['%', '2', '0']
            overwrite_index -= 3
        else:
            overwrite_index -= 1
            string[overwrite_index] = string[i]

my_test = list('Mr John Smith    ')
my_test2 = list('   s d  f               ')
URLify(my_test, 13)
URLify(my_test2, 10)
print(''.join(my_test))
print(''.join(my_test2))

"""
Time: O(n)
Space: O(n)
solution is a little bit unreadable
    the 3's seem hardcoded but are just related to '%20'
we could abstract the solution so whitespaces can be replaced by anything and less hardcoding
    this assumes the length is true length
"""


"""
Learnings
1. look at the problem from all angles, don't be satisfied with first thing that comes to mind
    e.g. front -> back, back -> front, etc
2. range(start, stop (exclusive), step)
"""