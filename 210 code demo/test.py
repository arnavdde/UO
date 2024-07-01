# ["y", "bl", "red","pinp", "white", "greeg", "liml"] --> 3

'''
string checker(input_str:list) -> int
the goal of the function is to check each string in a given list
for each string that is longer than 3 chars, check if the first and last character are the same
i += 1

examples

>>> 
'''

def string_checker(input_list):
    counted_strings = 0
    for a_string in input_list:
        if len(a_string) >= 3 and a_string[0] == a_string[-1]:
                counted_strings += 1
    return counted_strings




print(string_checker(["y", "bl", "red","pinp", "white", "greeg", "liml"])) # -> 3