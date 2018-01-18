# Author:           Jaap Kanbier
# Student number:   s1100592
# Assignment:       Forsyth-Edwards notatie - https://dodona.ugent.be/nl/exercises/867899652/

from string import punctuation


def fen2grid(fen_string, *optional_spec_char):
    # when there is a optional argument present check its validity, letters are not allowed
    if optional_spec_char:
        # since optional_spec_char is an array we only need to use the first character
        # any other passed arguments are irrelevant
        assert optional_spec_char[0] in punctuation, "Please use valid characters for spacing!"
        spacing_char = optional_spec_char[0]
    else:
        spacing_char = "*"

    # set up a variable to append values to in a loop
    grid_string = ''

    for char in fen_string:
        if char == '/':
            grid_string += '\n'
        elif char.isdecimal():
            # when a character is a number that means spacing
            for space in range(int(char)):
                # iterate and print the separation character
                grid_string += spacing_char
        # when it is not a number we can simply append
        else:
            grid_string += char

    return grid_string


def grid2fen(grid_string, *optional_spec_char):
    if optional_spec_char:
        assert optional_spec_char[0] in punctuation, "Please use valid characters for spacing!"
        spacing_char = optional_spec_char[0]
    else:
        spacing_char = "*"

    # set a variable to be returned and appended to
    fen_string = ''
    number_of_spaces = 0

    for char in grid_string:
        if char == spacing_char:
            # we increase the number of spaces for every spec char
            number_of_spaces += 1
        elif char.isalpha():
            # when a letter is about to be added we check if spacing is zero
            if number_of_spaces != 0:
                # if not, the amount of space needs to be added since it has ended
                fen_string += str(number_of_spaces)
                # also the amount of spaces is reset
                number_of_spaces = 0
            fen_string += char
        elif char == '\n':
            # the same goes for when the end of a line is reached
            if number_of_spaces != 0:
                fen_string += str(number_of_spaces)
                number_of_spaces = 0
            fen_string += '/'

    return fen_string


if __name__ == '__main__':
    print(fen2grid('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'))
    print(fen2grid('rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR', '.'))
    print(fen2grid('rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR', '+'))
    rooster = '''rnbqkbnr
    pppppppp
    ********
    ********
    ********
    ********
    PPPPPPPP
    RNBQKBNR'''
    print(grid2fen(rooster))
    print(grid2fen(fen2grid('rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR')))
    print(grid2fen(fen2grid('rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR', '.'), '.'))
    print(grid2fen(fen2grid('rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R', '+'), '+'))