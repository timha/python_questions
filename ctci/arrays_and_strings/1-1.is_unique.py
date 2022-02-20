"""
    an algorithm to determine if a string has all unique characters
"""
def is_unique(input_string):
    checked_chars = set()
    for char in input_string:
        if char not in checked_chars:
            checked_chars.add(char)
        else:
            return False
    return True

print(is_unique("dsfghhghg"))
print(is_unique("qweroiudkcm"))

"""
    without the use of additional data structure
"""
def is_unique_2(input_string):
    for i in range(len(input_string)):
        for j in range(i + 1, len(input_string), 1):
            if input_string[i] == input_string[j]:
                return False
    return True

print(is_unique_2("dsfghhghg"))
print(is_unique_2("qweroiudkcm"))


"""
    Learning
    1. ask questions
        is string ASCII or unicode? 
            e.g. ASCII only has 128 characters, if string is 130 length then it can't be unique
            e.g. use array and use character ASCII values as indexes
    2. bit vector
    3. sort first (may take require additional space)
"""