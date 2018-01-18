# Author:           Jaap Kanbier
# Student number:   s1100592
# Assignment:       Formule 1 - https://dodona.ugent.be/nl/exercises/1236821040/

# this script will check three variables and define a string based on those
# the output contains the location , the amount of laps driven and the total distance
# the input variables contain the following:
# - string of the name of the contest
# - float in km of the distance of one lap of the track
# - float in minutes of the average time to drive a lap


def take_user_input():
    # the input is define in 3 lines of text
    user_location = input("Where does the race take place? ")
    user_single_lap_distance = input("What is the distance of a single lap? ")
    user_single_lap_time = input("How much minutes does an average lap take to complete? ")

    # put all user input in an array to be passed around
    user_list = [user_location, user_single_lap_distance, user_single_lap_time]

    # this data is passed to be converted for calculations
    convert_user_input(user_list)


def convert_user_input(user_list):
    # convert the second and third strings to float values for calculations
    user_list[1] = float(user_list[1])
    user_list[2] = float(user_list[2])

    # check if the race location is Monaco
    # if so, all other algorithms can be skipped and output is predetermined
    check_for_monaco(user_list)


def check_for_monaco(user_list):
    if user_list[0] == "Monaco":
        # the location is Monaco: the output is set and generated
        laps_amount = 78
        distance_amount = laps_amount * user_list[1]
        generate_output(user_list[0], laps_amount, distance_amount)
    else:
        # when the location is not Monaco, the rest of the script will run
        calculate_output(user_list)


def calculate_output(user_list):
    # the minimum distance covered needs to be 305 km
    # however, the maximum amount of time spend racing can be 2 hours
    # when it runs longer the current round will be finished

    # appoint user_input to readable variables
    single_lap_distance = user_list[1]
    single_lap_time = user_list[2] * 60  # converts minutes to seconds

    # the first information needed is the expected amount of driven laps
    # this information can then be passed by different checks
    laps_amount = calculate_laps_amount(single_lap_distance)

    # check if the maximum racing time isn't exceeded
    max_race_time = 2 * 60 * 60  # max time in seconds
    est_race_time = calc_race_time(laps_amount, single_lap_time)
    # if the race doesnt exceed the max time, laps_amount needs no alteration
    if est_race_time > max_race_time:
        # a new amount of laps is calculated based of time
        laps_amount = laps_amount_by_time(max_race_time, single_lap_time)

    # the total driven distance is based of the max allowed laps
    # multiplied by the distance of a single lap
    distance_amount = laps_amount * single_lap_distance

    # convert the lap_amount from float to integers
    laps_amount = int(laps_amount)
    # round off total race distance to max 3 decimals
    distance_amount = round(distance_amount, 3)

    # pass the final results to the output generator
    generate_output(user_list[0], laps_amount, distance_amount)


def calculate_laps_amount(single_lap_distance):
    # get the minimum amount of laps driven by floor division
    laps_amount = 305 // single_lap_distance
    # if there is a remainder add 1 to the lap_amount
    # this is to finish the current lap and not end halfway
    if (305 % single_lap_distance) != 0:
        laps_amount += 1

    return laps_amount


def calc_race_time(laps_amount, lap_time):
    # calculate the total race time in seconds
    race_time = laps_amount * lap_time

    return race_time


def laps_amount_by_time(max_race_time, single_lap_time):
    # divide the max race time by a single lap time
    # discard the remainder since there are only whole laps
    corrected_lap_amount = max_race_time // single_lap_time

    # if there is a remainder, the final lap will be finished
    # thus an extra lap is added
    if (max_race_time % single_lap_time) != 0:
        corrected_lap_amount += 1

    return corrected_lap_amount


def generate_output(location_name, laps_amount, distance_amount):
    # the string with the result is composed
    output = ("The big price of %s will be driven in %s laps (%s km)."
              % (location_name, laps_amount, distance_amount))

    # display the result
    print(output)


# this is where the script starts to run
if __name__ == '__main__':
    take_user_input()
