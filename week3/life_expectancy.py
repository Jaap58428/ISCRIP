# Author:           Jaap Kanbier
# Student number:   s1100592
# Assignment:       Life Expectancy - https://dodona.ugent.be/en/exercises/849566952/
# Purpose:          Estimate the age a person will become depending on a set of conditions.

# Depending on five arguments passed to a function it will modify the average of 70
# sex: a string that indicates the sex of the person (man or woman)
# smoker: a Boolean value that indicates whether the person smokes or not
# sports: an integer that indicates how many hours the person exercises
# alcohol: an integer that indicates the amount of glasses of alcohol the person drinks a week
# fast_food: a Boolean value that indicates how much fast food is eaten


def life_expectancy(sex, smoker, sports, alcohol, fast_food):
    # the default average life expectancy is 70
    expected_age = 70

    print(sex, smoker, sports, alcohol, fast_food)

    # modify the expected age for every argument
    expected_age = modify_sex(expected_age, sex)
    expected_age = modify_smoker(expected_age, smoker)
    expected_age = modify_sports(expected_age, sports)
    expected_age = modify_alcohol(expected_age, alcohol)
    expected_age = modify_fast_food(expected_age, fast_food)

    # display the resulting life expectancy
    print(expected_age)


def modify_sex(expected_age, sex):
    # if the user is a woman 4 years are added
    if sex == 'woman':
        expected_age += 4
    return expected_age


def modify_smoker(expected_age, smoker):
    # if the user smokes 5 years are subtracted, otherwise 5 added
    if smoker:
        expected_age -= 5
    else:
        expected_age += 5
    return expected_age


def modify_sports(expected_age, sports):
    # if the user doesn't sport at all subtract 3 years
    if sports == 0:
        expected_age -= 3
    # add the amount of sporting to the expected age
    # since zero doesn't modify the value unwanted this also works
    expected_age += sports
    return expected_age


def modify_alcohol(expected_age, alcohol):
    # if the user doesn't drink any alcohol we add 2 years
    if alcohol == 0:
        expected_age += 2
    # otherwise we subtract 0.5 years for every glass over 7 a week
    elif alcohol > 7:
        expected_age -= ((alcohol - 7) / 2)
    return expected_age


def modify_fast_food(expected_age, fast_food):
    # if the user doesn't eat fast food often we add 3 years
    if not fast_food:
        expected_age += 3
    return expected_age


if __name__ == '__main__':
    life_expectancy(sex='man', smoker=True, sports=2, alcohol=10, fast_food=True)
    life_expectancy(sex='man', smoker=True, sports=5, alcohol=5, fast_food=True)
    life_expectancy(sex='woman', smoker=False, sports=5, alcohol=0, fast_food=False)
    life_expectancy(sex='woman', smoker=False, sports=3, alcohol=14, fast_food=True)
    life_expectancy(sex='man', smoker=False, sports=4, alcohol=4, fast_food=False)
