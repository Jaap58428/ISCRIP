# Author:           Jaap Kanbier
# Student number:   s1100592
# Assignment:       Double Dutch - https://dodona.ugent.be/nl/exercises/1153066363/


def medeklinkers(file_loc):
    file_dict = {}

    # after the file code block is done it closes
    with open(file_loc) as file:
        for line in file:
            # separate every line into different a tuple with key and value
            (key, val) = line.split()
            # every key is allocated a value
            file_dict[key] = val

    keys = file_dict.keys()
    # check if all conditions are met
    # the tuple approach in the previous code block already made sure there are no duplicates

    # if any of the keys is a vowel it returns false
    vowels_present = True
    for char in ('a', 'e', 'i', 'o'):
        if char in keys:
            vowels_present = False

    # returns false when the first letter of the value doesnt match the key
    invalid_line = True
    for char in keys:
        if not file_dict[char].startswith(char):
            invalid_line = False

    # run over all needed characters, when one isn't present it returns false
    missing_lines = True
    needed_chars = ('b', 'c', 'd', 'f', 'g', 'h', 'j',
                    'k', 'l', 'm', 'n', 'p', 'q', 'r',
                    's', 't', 'v', 'w', 'x', 'y', 'z',)
    for char in needed_chars:
        if char not in file_dict:
            missing_lines = False

    assert vowels_present and invalid_line and missing_lines, "ongeldige vertaling"

    return file_dict


def vertaalWoord(trans_string, dd_dict):
    # a set of vowels
    vowels = ('a', 'e', 'i', 'o', 'A', 'E', 'I', 'O')
    # variable to hold result
    result_list = []
    # iterate over the string_input
    for char in trans_string:
        # when it is a vowel it doesnt need translation
        if char in vowels:
            result_list.append(char)
        # otherwise transform and append
        else:
            result_list.append(dd_dict[char])

    # now we need to filter out the doubles
    result_without_doubles = []
    # keep track of which index needs to be removed
    del_index = []
    # when there are duplicate letters -> modify
    for item in range(len(result_list)):
        # check every letter for its previous one and is a vowel
        if result_list[item] == result_list[item - 1] and result_list[item] in vowels:
            # regarding if it's uppercase we appoint a prefix
            if result_list[item][0].isupper():
                prefix = 'Squat'
            else:
                prefix = 'squat'
            # set up the new value
            result_without_doubles.append(prefix + result_list[item].lower() + 'h')
            # save the duplicate index that needs to be removed
            del_index.append(item - 1)
        # when conditions arent met we just append it to the next list
        else:
            result_without_doubles.append(result_list[item])
    # loop over deletable items and take them from the result
    for index in del_index:
        del result_without_doubles[index]

    # finally convert the list into a string and pass it back
    return ''.join(result_without_doubles)


def vertaal(trans_string, dd_dict):
    from string import punctuation

    # setup a translation so all punctuation can be removed
    # this prevents any commas or periods to get taken into translation
    translator = str.maketrans('', '', punctuation)
    # pass the input into the translation
    bare_list = trans_string.translate(translator)
    # split it over any spaces left
    trans_list = bare_list.split(' ')

    # set up variable to hold Double Dutch translations
    raw_translation = ''
    for word in trans_list:
        # when a word is a single vowel it does not need translation
        if word in ('a', 'e', 'i', 'o', 'A', 'E', 'I', 'O'):
            raw_translation += word + ' '
        # any other word needs to passed through Double Dutch translation
        else:
            raw_translation += vertaalWoord(word, dd_dict) + ' '

    # add a dot at the end of the string
    print_result = list(raw_translation)
    print_result[-1:] = '.'

    # join the list together into a string
    return ''.join(print_result)


if __name__ == '__main__':
    dutchLetter = medeklinkers('dutchLetters.txt')
    print(dutchLetter['s'])
    print(dutchLetter['q'])
    print(dutchLetter['d'])
    # print(dutchLetter['e'])
    print(vertaalWoord('took', dutchLetter))
    print(vertaalWoord('BAMBOO', dutchLetter))
    print(vertaalWoord('Yesterday', dutchLetter))
    print(vertaal('I took a walk to the park yesterday.', dutchLetter))