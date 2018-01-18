# Author:           Jaap Kanbier
# Student number:   s1100592
# Assignment:       Game of Life - https://dodona.ugent.be/en/exercises/511272034/

# this script will modify and interact with a set of values, called a generation
# this generation is a set of lists emerging into a 2d matrix of booleans
# each item represents a cell which is either alive (True, X) or dead (False, O)
# the script can display this generation, get the number or neighbouring cells and iterate to a new generation
# this new generation is based of a set of rules applied on the old generation

# a cell with 2 or 3 neighbours will stay alive
# a cell with less then 2 or more then 3 neighbours will die
# a cell with exactly 3 neighbours will come to live

# these rules can be applied to generate patterns based of certain initial conditions


def show_generation(print_generation):
    # every cell in the generation is represented by either alive 'X' or dead 'O'
    # loop over all the items and check its value to then print its corresponding character
    for cell_ver in range(len(generation)):
        for cell_hor in range(len(generation)):
            # for readability we put a space between every character
            print(" ", end='')
            if print_generation[cell_ver][cell_hor]:
                # if the coordinates are True we print X
                print("X", end='')
            else:
                # otherwise a letter O is printed
                print("O", end='')
        # we only want to go to a new line when the vertical line is done
        print('')


def number_of_neighbours(gen_list, row, column):

    # set a variable to hold the number of neighbouring cells
    num_of_neigh = 0

    # set te highest value a value can be
    # if a value is either zero or this it is against the edge of the generation
    # this means we don't have (and aren't possible) to check beyond this point
    gen_size = len(gen_list) - 1

    # if the value isn't the first row, check the row above it
    if (row != 0) and (gen_list[(row - 1)][column]):
        num_of_neigh += 1
    # if the value isn't the last row, check the row below it
    if (row != gen_size) and (gen_list[(row + 1)][column]):
        num_of_neigh += 1
    # if the value isn't the first column, check the column before it
    if (column != 0) and (gen_list[row][(column - 1)]):
        num_of_neigh += 1
    # if the value isn't the last column, check the column after it
    if (column != gen_size) and (gen_list[row][(column + 1)]):
        num_of_neigh += 1
    # if the value isn't in the first row and column (top left), check the left above it
    if (row != 0) and (column != 0) and (gen_list[(row - 1)][(column - 1)]):
        num_of_neigh += 1
    # if the value isn't in the last row and column (bottom right), check the right bellow it
    if (row != gen_size) and (column != gen_size) and (gen_list[(row + 1)][(column + 1)]):
        num_of_neigh += 1
    # if the value isn't last row and first column, check the left bellow it
    if (row != gen_size) and (column != 0) and (gen_list[(row + 1)][(column - 1)]):
        num_of_neigh += 1
    # if the value isn't first row and last column, check the right above it
    if (row != 0) and (column != gen_size) and (gen_list[row - 1][column + 1]):
        num_of_neigh += 1

    return num_of_neigh


def next_generation(old_gen):

    # lists keep their references to their origin, for this reason we generate tuples out of it
    # this way we can keep track of the statistics of the old gen while generation the new one
    # this conversion is both applied to the entire generation and its sub lists
    prev_gen = tuple(map(tuple, old_gen))
    # a new generation is passed back, although this might not be needed for reasons mentioned above
    new_gen = old_gen

    # for every row we want to check the amount of times the size of the generation...
    for row in range(len(old_gen)):
        # check in each row every column...
        for column in range(len(old_gen)):
            # check the living conditions for this cell
            gen_condition = number_of_neighbours(prev_gen, row, column)
            # depending on these conditions it MIGHT change
            if gen_condition == 3:
                # it can be born when there are exactly 3 neightbours
                new_gen[row][column] = True
            elif gen_condition > 3 or gen_condition < 2:
                # it can die when there are more then 3 or less then 2 neighbours
                new_gen[row][column] = False

    return new_gen


if __name__ == '__main__':
    # set up a generation with the first column True but all other False
    # with a size of 6 fields or cells big
    generation = [[True] + [False] * 7 for _ in range(6)]

    # display the first generation on screen without making it evolve
    show_generation(generation)

    # show the number of neighbouring cells for the first row and the first column
    print(number_of_neighbours(generation, 0, 0))
    # the same for the second row and second column
    print(number_of_neighbours(generation, 1, 1))
    # the same for the third row and third column
    print(number_of_neighbours(generation, 2, 2))

    # go over every cell of a generation and check its amount of neighbours
    # depending on this value the cell either dies, comes alive or stays unchanged
    next_gen = next_generation(generation)
    # then after iterating over its evolution process show it on screen
    show_generation(next_gen)

    # repeat this process three more times
    next_gen = next_generation(generation)
    show_generation(next_gen)
    next_gen = next_generation(generation)
    show_generation(next_gen)
    next_gen = next_generation(generation)
    show_generation(next_gen)
