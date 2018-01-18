# Author:           Jaap Kanbier
# Student number:   s1100592
# Assignment:       Slaapkwaliteit - https://dodona.ugent.be/nl/exercises/1795071955/

# a script that calculates a ideal time to wake up for the user
# this is done by taking the time the user goes to sleep and the desired earliest waking time
# the output is a time after the chosen waking time based of a multiplication of 90 minutes

# concretely the input is done in 4 different values representing
# hours, minutes (bed time) and hours, minutes (minimal waking time)


def take_user_input():

    # ask the user for all the required values to run the script
    bed_time_hours = input("What is your bedtime in hours? ")
    bed_time_minutes = input("What is your bedtime in minutes? ")
    wake_time_hours = input("What time do you want to wake at minimum in hours? ")
    wake_time_minutes = input("What time do you want to wake at minimum in minutes? ")

    # put all the values in a list so it is easy to pass around
    user_input = [bed_time_hours, bed_time_minutes, wake_time_hours, wake_time_minutes]

    # convert strings to integers
    parse_user_input(user_input)


def parse_user_input(user_input):

    # in order to check if the input is correct they need to be converted to integers
    user_data = list(map(int, user_input))

    check_user_input(user_data)


def check_user_input(user_data):

    # unless proven otherwise the input is incorrect
    input_hours = False
    input_minutes = False

    # the input cant fall outside of the 24:00 hours format
    # so the amount of minutes needs to be 0 to 59 and hours 0 to 23
    if user_data[0] in range(24) and user_data[2] in range(24):
        input_hours = True
    if user_data[1] in range(60) and user_data[3] in range(60):
        input_minutes = True

    # if both values are correct the program will start to calculate
    if input_hours and input_minutes:
        calculate_wake_time(user_data)


def calculate_wake_time(user_data):

    # set user_data to readable variables
    sleep_hours = user_data[0]
    sleep_minutes = user_data[1]
    min_wake_hours = user_data[2]
    min_wake_minutes = user_data[3]

    # convert minutes to hours so that one single value is used to calculate
    sleep_time = sleep_hours + sleep_minutes / 60
    min_wake_time = min_wake_hours + min_wake_minutes / 60

    # the slept time is a continuous time span, we can add 24 to wake_time
    # this creates a good format to calculate total sleeping time
    total_sleep_time = (24 + min_wake_time) - sleep_time

    good_sleep_time = 0

    while good_sleep_time > total_sleep_time:
        good_sleep_time += 1.5

    # convert the corrected waking time back to separate hours and minutes
    wake_hours = good_sleep_time // 1
    wake_minutes = (good_sleep_time % 1) * 60

    format_wake_time(wake_hours, wake_minutes)


def format_wake_time(wake_hours, wake_minutes):

    # set the wake time to correct format
    print_hours = str(int(wake_hours))
    print_minutes = str(int(wake_minutes))

    # add leading zeroes if needed
    if wake_hours < 10:
        print_hours = ("0" + print_hours)
    if wake_minutes < 10:
        print_minutes = ("0" + print_minutes)

    # compile the result
    result = print_hours + ":" + print_minutes

    # show the result on screen
    print(result)


if __name__ == '__main__':
    take_user_input()