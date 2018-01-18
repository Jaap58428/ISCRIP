# Author:           Jaap Kanbier
# Student number:   s1100592
# Assignment:       Interessante getallen - https://dodona.ugent.be/nl/exercises/211647828/

# a script that looks for 'interesting numbers'
# the input is a set of 50 or less numbers, each an integer between 0 and 100 (including 100)
# the output is a set representing the input containing no leading zeroes and is both
# - dividable by its representing input
# - the sum of its individual digits equal to its representing input


from random import randint


def take_user_input():
    # ask the user for an input
    user_input = input("Give a natural number (<= 50): ")

    # make a natural number out of the user input
    user_input = int(user_input)

    # check if the input passes the requirements
    if user_input <= 50:
        generate_list(user_input)
    else:
        # if not the script will tell the user
        print("Please give a natural number bellow or equal to 50.")


def generate_list(user_input):

    # declare an array to hold each test case
    test_cases = []

    # generate random integers for the amount of user_input
    for single_case in range(0, user_input):
        # I changed the scale of the possible test cases from 100 to 40
        # this still proves the concept but significantly decreases operation time
        test_cases.append(randint(1, 40))

    calculate_results(test_cases)


def calculate_results(test_cases):

    # an array with solutions is declared to contain all solutions
    results = []

    for single_test in test_cases:
        # the solution hasn't been found yet
        solution_not_found = True

        # we are looking for the smallest solution so we increment upwards
        # the smallest division is its own value
        possible_solution = single_test

        # as long as the solution hasn't been found we keep iterating
        while solution_not_found:

            # in case both are passed the result is added to the results array
            # the while loop is ended by setting its condition to False
            if check_requirement_sum(single_test, possible_solution):
                results.append(possible_solution)
                solution_not_found = False
            else:
                # the condition isn't met, increase possible_solution by one for another iteration
                # incrementation is done by the input so it is always dividable by this same input
                possible_solution += single_test

    # after all iterations both the results and test cases are passed for output
    generate_output(results, test_cases)


def check_requirement_sum(single_test, possible_solution):

    # change the possible solution into a string so it can be iterated over
    string_solution = str(possible_solution)

    # convert the string into a list of digits
    list_of_digits = list(string_solution)

    # convert the list of strings into a list of integers
    digit_list = list(map(int, list_of_digits))

    # the starting sum of digits is always zero
    sum_of_digits = 0

    # add every single digit of the list to variable
    for single_digit in digit_list:
        sum_of_digits += single_digit

    # if the sum is equal to the test case it passes this condition
    return sum_of_digits == single_test


def generate_output(result, test_cases):

    # in order for the user to know what was tested for we show the generated input
    print("Test cases:")
    for line in test_cases:
        print(line)

    # these are the results for each individual test case
    print("The results for these cases:")
    for line in result:
        print(line)


# start the script
if __name__ == '__main__':
    take_user_input()