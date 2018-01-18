# Author:           Jaap Kanbier
# Student number:   s1100592
# Assignment:       Vierkant van Pascal - https://dodona.ugent.be/nl/exercises/1799377797/


def vierkant(size, *starting_number):
    # wanneer er een optioneel argument aanwezig is zal deze worden toegewezen als start getal
    if starting_number:
        start = starting_number[0]
    # zo niet dan is 1 het standaard getal
    else:
        start = 1

    # initieer het raster
    raster = [[start for x in range(size)] for y in range(size)]

    # start bij elke rij en kolom op de 2e index
    for row in range(1, size):
        for number in range(1, size):
            # neem voor elk raster punt het getal er boven en links van en tel deze op
            raster[row][number] = raster[row - 1][number] + raster[row][number - 1]

    return raster


def paden(size, *start):
    if start:
        # wanneer er een argument aanwezig is geven we die door
        raster = vierkant(size, start[0])
    else:
        raster = vierkant(size)

    # zet een integer die be7paald hoe lang elke element moet zijn
    max_string_size = len(str(raster[size - 1][size - 1])) + 1

    result = ''

    for row in range(size):
        for column in range(size):
            # bepaal het toe te voegen element
            new_item = str(raster[row][column])
            # zolang het element niet lang genoeg is voegen we spaties toe
            while len(new_item) < max_string_size:
                new_item = ' ' + new_item
            result += new_item
        # aan het einde van een rij voegen we een nieuwe regel toe
        result += '\n'

    return result


if __name__ == '__main__':
    vierkant(3)
    vierkant(3, 100)
    vierkant(4)
    print(paden(3))
    print(paden(3, 100))
    print(paden(4))
    print(paden(6))
    print(paden(8))
    print(paden(10))