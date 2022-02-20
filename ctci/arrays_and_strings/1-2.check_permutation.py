"""
    given two strings, decide if one is a permutation of the other
"""

"""
    Initial thoughts
        if lengths are different -> False
        sort both strings first, check char by char equality
        if not allowed to sort, add chars of str1 to array, remove them as you encounter them in array
            ord()
"""


# solution with sorting
def check_permutation_with_sort(str1, str2):
    if len(str1) != len(str2):
        return False

    str1 = sorted(str1)
    str2 = sorted(str2)

    # standard implementation with using zip()
    #for i in range(len(str1)):
    #    if str1[i] != str2[i]:
    #        return False

    # using zip()
    for c1, c2 in zip(str1, str2):
        if c1 != c2:
            return False
    
    return True

print(check_permutation_with_sort("sdfjkhsjkhiuwhfsd", "sdfjkhsjkhiuwhfsdm"))
print(check_permutation_with_sort("abcdefghjiklsjkhc", "abcdefghjiklsjkhc"))



# solution without sorting
def check_permutation_no_sort(str1, str2):
    if len(str1) != len(str2):
        return False
    
    str1_chars = [0] * 128 # assuming ASCII
    for char in str1:
        str1_chars[ord(char)] += 1
    
    for char in str2:
        str1_chars[ord(char)] -= 1
        if str1_chars[ord(char)] < 0:
            return False
    
    return True

print(check_permutation_no_sort("sdfjkhsjkhiuwhfsd", "sdfjkhsjkhiuwhfsdm"))
print(check_permutation_no_sort("abcdefghjiklsjkhc", "abcdefghjiklsjkhc"))