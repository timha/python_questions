"""
three types of edits: insert, remove, or replace a character
given two strings, determine if they are 1 or 0 edits within each other
"""

"""
Initial thoughts
    are there limitations to strings? ASCII? Unicode? only letters?
    check absolute value of difference in length of strings is < 2. otherwise False
    could iterate through both strings (maybe gets tricky?)
    could use a set. doesn't work well with duplicates letters
    if ascii or extended ascii, can use 128 or 256 length array and store counts in indexes
    if unicode then it gets ugly. hashmap but it doesn't work well with long strings
    sort? doesn't seem particularly helpful
    iterating through both strings seems a good enough start
        need to control how to iterate.
        if lengths are unequal and we encounter 1 diff then False because the extra character is another diff
"""

def one_away(s1, s2):
    length_diff = len(s1) - len(s2)
    if abs(length_diff) > 1:
        return False

    if length_diff < 0:
        temp_string = s1
        s1 = s2
        s2 = temp_string
    
    num_edits = 0
    small_index = 0
    for i in range(len(s2)):
        if s1[i] != s2[small_index]:
            num_edits += 1
            if num_edits > 1:
                return False
            if length_diff != 0:
                small_index -= 1
        small_index += 1
    
    return True

print(one_away('pale', 'ple'))
print(one_away('pale', 'bale'))
print(one_away('pale', 'bake'))
print(one_away('lll', 'llok'))
