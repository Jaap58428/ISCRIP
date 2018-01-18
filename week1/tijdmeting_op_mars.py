# Author:           Jaap Kanbier
# Student number:   s1100592
# Assignment:       https://dodona.ugent.be/nl/exercises/1813154454/

# this program will translate an input to an output
# specifically it will take the amount of days on the planet Mars
# and will convert them to Earth days
# On average a day on Mars takes 24 hours, 39 minutes and 35.244 seconds

# this is a placeholder variable for the input
user_input = 123

# seconds are the smallest unit, converting all to seconds
# 1 sol day is
sol_day_in_seconds = 35.244 + 39 * 60 + 24 * 60 * 60
earth_day_in_seconds = 24 * 60 * 60
earth_hour_in_seconds = 60 * 60
earth_minute_in_seconds = 60

# convert input (mars seconds) to output (earth seconds)
total_earth_seconds = user_input * sol_day_in_seconds

# divide the total of earth seconds by the amount of seconds per day
# both the floor division and remainder are stored
days = total_earth_seconds // earth_day_in_seconds
days_remainder = total_earth_seconds % earth_day_in_seconds

# the remainder of the above also gets divided
hours = days_remainder // earth_hour_in_seconds
hours_remainder = days_remainder % earth_hour_in_seconds

minutes = hours_remainder // earth_minute_in_seconds
minutes_remainder = hours_remainder % earth_minute_in_seconds

# this final floor division is here for exhaustion
# the decimal counting system already makes this single units
# in case of hexadecimal or binary counting it could be modified
seconds = minutes_remainder // 1

# converting all results to integers and placing them in strings
output_days = (str(int(days)) + " day")
output_hours = (str(int(hours)) + " hour")
output_minutes = (str(int(minutes)) + " minute")
output_seconds = (str(int(seconds)) + " second")

# setting the output segments to single or plural units
# meaning either second or secondS, either day or dayS...
units = [days, hours, minutes, seconds]
outputs = [output_days, output_hours, output_minutes, output_seconds]

# to fetch each item in the list of outputs there is another iterator 'arr'
arr = 0
for amount in units:
    if amount != 1:
        outputs[arr] = (outputs[arr] + "s")
    arr += 1

# setting up the string to be printed as output
output = (str(user_input) + " sol = " +
          outputs[0] + ", " +
          outputs[1] + ", " +
          outputs[2] + " and " +
          outputs[3])

# show the result on screen
print(output)