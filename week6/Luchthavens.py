# Author:           Jaap Kanbier
# Student number:   s1100592
# Assignment:       Luchthavens - https://dodona.ugent.be/nl/exercises/1748605282/


def leesLuchthavens(bestandsnaam):
    # set variable to store dict items
    air_dict = {}
    # use file data
    with open(bestandsnaam) as file_data:
        # separate every line and start from index 1
        lines = file_data.read().splitlines()[1:]
        # every line gets the same transformation
        for entry in lines:
            # split the item line on tabs
            set_item = entry.split('\t')
            # the first item will be the key after trimming
            key = set_item[0][1:4]
            # the rest will be a tuple as the value
            value = (float(set_item[1]), float(set_item[2]), set_item[3], set_item[4])
            # appoint the set to the dict
            air_dict[key] = value
    return air_dict


def afstand(code1, code2, luchthavens_dict):
    # this variable is a given
    earth_radius = 6372.795

    # give all relevant data meaningful variable names
    start_hor = luchthavens_dict[code1][0]
    start_ver = luchthavens_dict[code1][1]
    end_hor = luchthavens_dict[code2][0]
    end_ver = luchthavens_dict[code2][1]

    # how to convert degrees to radians
    # 1 degree = pi / 180 = 0.005555556 pi = 0.01745329252 rad
    from math import pi
    radian_factor = pi / 180

    # convert all starting points to radians
    b1 = start_hor * radian_factor
    l1 = start_ver * radian_factor
    b2 = end_hor * radian_factor
    l2 = end_ver * radian_factor

    # apply partial formula on values above and bellow line
    from math import cos
    from math import sin
    over_line = (cos(b2)*sin(l1 - l2)) ** 2 + (cos(b1)*sin(b2) - sin(b1)*cos(b2)*cos(l1 - l2)) ** 2
    under_line = sin(b1) * sin(b2) + cos(b1) * cos(b2) * cos(l1 - l2)

    # finish formula
    from math import sqrt
    from math import atan
    return earth_radius * atan(sqrt(over_line) / under_line)


def tussenlanding(code1, code2, luchthavens_dict, *opt_reikwijdte):
    # check if a optional argument is passed to the function
    if opt_reikwijdte:
        # if so, this will be the flying radius
        reikwijdte = opt_reikwijdte[0]
    else:
        # if not, the default is 4000 km
        reikwijdte = 4000

    # a function call is returned as None when the total distance is within reach or out of reach after a single stop
    single_distance = afstand(code1, code2, luchthavens_dict)
    if single_distance < reikwijdte or single_distance > reikwijdte * 2:
        return None

    # create a list of valid destinations within the flying radius
    valid_stops_ac = []
    valid_stops_cb = []
    for mid_stop in luchthavens_dict:
        distance_ac = afstand(code1, mid_stop, luchthavens_dict)
        distance_cb = afstand(code2, mid_stop, luchthavens_dict)
        if distance_ac <= reikwijdte:
            valid_stops_ac.append(mid_stop)
        if distance_cb <= reikwijdte:
            valid_stops_cb.append(mid_stop)

    # look for overlap in the both lists, these are potentially valid mid stops
    valid_overlap = set(valid_stops_ac).intersection(valid_stops_cb)

    # take the lowest value of valid_overlap
    # the shortest possible route needs to be bellow twice the flying span
    current_shortest_distance = reikwijdte * 2
    current_shortest_location = ''
    for possible_stop in valid_overlap:
        # the total of combined values needs to be the lowest
        distance_ac = afstand(code1, possible_stop, luchthavens_dict)
        distance_cb = afstand(code2, possible_stop, luchthavens_dict)
        if distance_ac + distance_cb < current_shortest_distance:
            current_shortest_distance = distance_ac + distance_cb
            current_shortest_location = possible_stop

    return current_shortest_location


if __name__ == '__main__':
    # function that takes a string as file location
    # it returns a dictionary of all airports and their metadata
    luchthavens = leesLuchthavens('luchthavens.txt')

    # print the entire dictionary
    print(luchthavens)

    # print the values of the key ADK, DCA and 4OM
    print(luchthavens['ADK'])
    print(luchthavens['DCA'])
    print(luchthavens['4OM'])

    # print the distance between airports using the function afstand()
    # this takes two keys and its dictionary and returns a distance in KM
    print(afstand('P60', 'MSN', luchthavens))
    print(afstand('ADK', 'DCA', luchthavens))

    # print the best route between to destinations given its maximum radius
    print(tussenlanding('ADK', 'DCA', luchthavens, 4000))