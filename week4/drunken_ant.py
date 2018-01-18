# Author:           Jaap Kanbier
# Student number:   s1100592
# Assignment:       Drunken Ant - https://dodona.ugent.be/en/exercises/276629077/

# an ant will move over a grid based of directional instructions
# these are ^ up, v down, < left and > right
# after an ant has walked over this sign it turns 90 degrees clockwise
# each grid is  size n, so both n long and wide and the ant moves from left bottom to top right
# the ant follow the direction of each location unless it points of the grid
# in this case the ant stays still and moves 90 degrees clockwise


def grid(grid_size, grid_string):
    # test if the size does compare to the product its actual length
    assert len(grid_string) / grid_size == grid_size, "invalid arguments"

    # set up an 2d list to insert the values in
    return_list = [[0 for column_item in range(grid_size)] for row_item in range(grid_size)]

    # parse the string into a list
    # the product of a double for loop to retrieve correct values
    get_list = list(grid_string)
    for row in range(grid_size):
        for column in range(grid_size):
            # to get the location of the get_list we have a product of the size and row
            # plus the column location of that particular row
            get_char = (row * grid_size) + column
            return_list[row][column] = get_list[get_char]
    return return_list


def text(grid_data):
    # set up a string to be returned
    grid_string = ''
    for row in range(len(grid_data)):
        for column in range(len(grid_data)):
            # replace the end-line after every print statement with space
            grid_string += (grid_data[row][column] + ' ')
        # after the row is done append a new line character
        grid_string += '\n'
    return grid_string


def step(grid_data, grid_location):
    # move from one position (argument 2) to another based of the grid_data
    # get the direction of the ant
    ant_direction = grid_data[grid_location[0]][grid_location[1]]

    # the highest index is the size minus one
    grid_size = len(grid_data) - 1

    # based of this value do one of 4 options
    if ant_direction == '^':
        # regardless of movement of the ant the pheromone is altered
        grid_data[grid_location[0]][grid_location[1]] = '>'
        # when the direction doesnt fall outside the grid we pass the new location
        if grid_location[0] != 0:
            return grid_location[0] - 1, grid_location[1]
        # otherwise we return the old one, but the pheromone is still altered
        else:
            return grid_location

    elif ant_direction == '>':
        grid_data[grid_location[0]][grid_location[1]] = 'v'
        if grid_location[1] != grid_size:
            return grid_location[0], grid_location[1] + 1
        else:
            return grid_location

    elif ant_direction == 'v':
        grid_data[grid_location[0]][grid_location[1]] = '<'
        if grid_location[0] != grid_size:
            return grid_location[0] + 1, grid_location[1]
        else:
            return grid_location

    elif ant_direction == '<':
        grid_data[grid_location[0]][grid_location[1]] = '^'
        if grid_location[1] != 0:
            return grid_location[0], grid_location[1] - 1
        else:
            return grid_location


def steps(grid_data):
    # set an array to hold a trivial amount of locations that the ant passes
    location_list = []

    # the grid can be any size
    max_position = len(grid_data) - 1

    # the ant always starts at the bottom left
    location = (max_position, 0)

    # as long as the destination isn't reached keep stepping
    while location != (0, max_position):
        location_list.append(location)
        location = step(grid_data, location)

    # the while loop stops the moment it reaches the destination so the final location is appended
    location_list.append(location)
    print(location_list)


if __name__ == '__main__':
    square = grid(4, '>>>>^<^v^v^^>>v>')
    print(text(square))
    print(step(square, (3, 0)))
    print(text(square))
    print(step(square, (3, 1)))
    print(text(square))

    square = grid(4, '>>>>^<^v^v^^>>v>')
    print(text(square))
    steps(square)
    print(text(square))

    # grid(4, '>>>>^<^v^v^>>v>')