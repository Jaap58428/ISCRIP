# Author:           Jaap Kanbier
# Student number:   s1100592
# Assignment:       Strong Passwords - https://dodona.ugent.be/en/exercises/417422714/

# purpose: print over a set of passwords for each a value of weak, moderate or strong
# this is based of a set of conditions that, if more are checked it is stronger
# 1-2 = weak, 3-4 = moderate, 5-6 = strong
# the input is a integer that indicates how many passwords will be checked
# followed by the set of passwords


def check_8char(string):
    # check if string is at least 8 characters long
    return len(string) >= 8


def check_uppercase(pw_string):
    from string import ascii_uppercase as uc
    # check if pw_string contains any uppercase letters
    return any(char in pw_string for char in uc)


def check_lowercase(pw_string):
    from string import ascii_lowercase as lc
    # check if pw_string contains any lowercase letters
    return any(char in pw_string for char in lc)


def check_decimal(pw_string):
    from string import digits as dec
    # check if pw_string contains any decimal digits
    return any(char in pw_string for char in dec)


def check_spec_char(pw_string):
    from string import punctuation as sc
    # check if pw_string contains any special characters
    return any(char in pw_string for char in sc)


if __name__ == '__main__':
    pass_amount = int(input("How many passwords do you want to check? "))

    pass_list = []

    for pass_string in range(pass_amount):
        pass_list.append(input("Please give the password you want to check: "))

    # go over the list of passwords and check for all conditions
    for pass_string in pass_list:

        # the strength (degree of checks passed) starts at zero
        pass_strength = 0

        # a boolean also is an integer of 0 (false) or 1 (true)
        # so we can increase the strength for every passed check
        pass_strength += check_8char(pass_string)
        pass_strength += check_uppercase(pass_string)
        pass_strength += check_lowercase(pass_string)
        pass_strength += check_decimal(pass_string)
        pass_strength += check_spec_char(pass_string)

        # print the corresponding value
        if pass_strength < 3:
            print("weak")
        elif pass_strength > 4:
            print("strong")
        else:
            print("moderate")