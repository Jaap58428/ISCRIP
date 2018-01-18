# Author:           Jaap Kanbier
# Student number:   s1100592
# Assignment:       https://dodona.ugent.be/nl/exercises/1576457755/

# this script will performs calculations on a set of euro coins
# the amount of euro coins is specified in the input
# each line represents respectively 1, 2, 5, 10, 20, 50 cents and 1 and 2 euros
# the output will be the total amount and the total sum of coins

user_input = '''123
12
432
12
532
0
3
9
'''

# this function puts every line into a list of strings
coin_list = user_input.splitlines()

# however to calculate with the values they need to be parsed to integers
# also the total amount of coins is added to total_coin_amount
total_coin_amount = 0
for coin_amount in coin_list:
    coin_amount = int(coin_amount)
    total_coin_amount += coin_amount

# we need to have a list of values representing each item of coin_list
# this is done in cents to later be converted in full euros
coin_values = [1, 2, 5, 10, 20, 50, 100, 200]

# each coin_list[X] needs to be multiplied by coin_values[X]
# this is then added to the total value of the coins
total_coin_value = 0
iteration = 0
for value in coin_values:
    total_coin_value += value * int(coin_list[iteration])
    iteration += 1

# convert total_coin_value from cents to euros
total_coin_value /= 100

# print the results to display
print(str(total_coin_amount) + "\n" + str(total_coin_value))
