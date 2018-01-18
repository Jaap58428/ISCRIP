# Author:           Jaap Kanbier
# Student number:   s1100592
# Assignment:       Mobile Synonyms - https://dodona.ugent.be/en/exercises/1858246142/
# Purpose:          Give the T9 decimal equivalent to a string of letters
#                   Check if the T9 equivalent is the same for multiple strings of letters

# this script has two methods: t9_convert and mobile_synonyms
# t9_convert will take a string of letters and turn it into its t9 notational input of decimal digits
# mobile_synonyms compares two strings of letters and compares if the outputs of t9_convert are equal


def t9_convert(word):
    # transform to lowercase to have uniform input
    word = word.lower()

    # build library of letter sets
    two_key = ['a', 'b', 'c']
    three_key = ['d', 'e', 'f']
    four_key = ['g', 'h', 'i']
    five_key = ['j', 'k', 'l']
    six_key = ['m', 'n', 'o']
    seven_key = ['p', 'q', 'r', 's']
    eight_key = ['t', 'u', 'v']
    nine_key = ['w', 'x', 'y', 'z']

    # setup a variable to hold the return value
    t9_equivalent = ''

    # build up the equivalent based on each letter
    for letter in word:
        if letter in two_key:
            t9_equivalent += '2'
        elif letter in three_key:
            t9_equivalent += '3'
        elif letter in four_key:
            t9_equivalent += '4'
        elif letter in five_key:
            t9_equivalent += '5'
        elif letter in six_key:
            t9_equivalent += '6'
        elif letter in seven_key:
            t9_equivalent += '7'
        elif letter in eight_key:
            t9_equivalent += '8'
        elif letter in nine_key:
            t9_equivalent += '9'
        else:
            print('Only use letters as input for this method!')

    return t9_equivalent


def mobile_synonyms(word_one, word_two):
    # return the comparison boolean for word_one versus word_two
    return t9_convert(word_one) == t9_convert(word_two)


if __name__ == '__main__':
    print(t9_convert('Banner'))
    print(t9_convert('succes'))
    print(t9_convert('rubber'))

    print(mobile_synonyms('succes', 'rubber'))
    print(mobile_synonyms('Monday', 'Friday'))
