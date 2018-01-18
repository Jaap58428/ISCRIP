# Author:           Jaap Kanbier
# Student number:   s1100592
# Assignment:       Paardensprong - https://dodona.ugent.be/nl/exercises/56374393/

# the purpose of this script is to take 2 positions on a chessboard (input)
# the first is the starting position of the chess piece 'horse'
# The second is the desired landing position of said piece
# the result is a string which notifies the user if this transition is possible

# take the user input and set the starting and ending position to variables
user_start = input("Give the starting location of the Horse: ")
user_end = input("Give the ending location of the Horse: ")

# debug variables
# user_start = "d4"
# user_end = "e6"

# split the start and end to horizontal and vertical values
start_pos = list(user_start)
end_pos = list(user_end)

# to calculate easily translate the ascii char to decimal
# 96 is subtracted so that a == 1, b == 2, etc.
# this assumes the input is always in lowercase characters
start_pos[0] = ord(start_pos[0]) - 96
end_pos[0] = ord(end_pos[0]) - 96

# also to calculate with the input all need to be integers
start_pos[1] = int(start_pos[1])
end_pos[1] = int(end_pos[1])

# the difference between the start_pos and end_pos needs to be either:
# 1 AND 2 OR 2 AND 1, so for example the coordinates
# (a to b) AND (4 to 6) OR (a to c) AND (4 to 5)

# two sets of valid outcomes that the if statements will check against
move_one = [1, -1]
move_two = [2, -2]

# by default the transition is false, unless it passes the checks
transition_valid = False
if ((start_pos[0] - end_pos[0]) in move_one) and ((start_pos[1] - end_pos[1]) in move_two):
    transition_valid = True
elif ((start_pos[0] - end_pos[0]) in move_two) and ((start_pos[1] - end_pos[1]) in move_one):
    transition_valid = True

# if the transition is legal a string will be set
if transition_valid:
    transition_valid_print = "can"
else:
    transition_valid_print = "can't"

# the output is compiled into a string
output = ("The horse " + transition_valid_print + " jump from " +
          user_start + " to " + user_end + ".")

# display the result
print(output)
