#!/usr/bin/env python3

# import functions that will be useful to this script below
from time import sleep,strftime

'''This calendar script will allow the user to interactively view, add, update, or delete events. It will continue
running until it is given input to stop and exit the script, which will allow the user to accomplish multiple tasks
in a single execution of the script.'''

print('Hello there!')
# set user name as a constant for greeting
user_name = input('Please enter your name.\n>> ')

# create dictionary for the storage of dates and events in the calendar
calendar = {}

# define welcome greeting function
def welcome():
    '''The welcome function serves as the introduction of the calendar script'''
    print(f'Welcome to the calendar, {user_name}.')
    print('The calendar is opening now.')
    sleep(1)
    # current date variable
    today = strftime('%A, %B %d, %Y')
    # current time variable
    time = strftime('%I:%M %p')
    print(f'Today is {today}.')
    print(f'The time is {time}.')
    sleep(1)
    print('What would you like to do?')

# next, we define the executor of our calendar
def start_calendar():
    '''The start_calendar function serves as the main executor of the calendar itself'''
    # call the welcome function
    welcome()
    # declare a variable that will keep our function looping with the 'while' loop
    start = True
    while start:
        # ask the user for input that will dictate what the script will do next within the loop
        user_choice = input('Please enter "A" to Add, "U" to Update, "V" to View, "D" to Delete, or "E" to Exit\n>> ')
        # convert the user input to uppercase for convenience
        user_choice = user_choice.upper()

        # the conditionals will designate what the next action is to be
        # view calendar
        if user_choice == 'V':
            if len(calendar.keys()) < 1:
                print('The calendar is currently empty.')
            else:
                print(calendar)

        # exit calendar script
        elif user_choice == 'E':
            start = False

        # update calendar
        elif user_choice == 'U':
            date = input('What date would you like to update?\n>> ')
            update = input('Enter the update you wish to add:\n>> ')
            calendar[date] = update
            print('The desired update has been added to your calendar.')
            print(calendar)

        # add to calendar
        elif user_choice == 'A':
            # while loop implemented to keep the try/except check going until the correct date conditions are met
            while True:
                try:
                    # add date - event to celendar
                    event = input('Please enter the event to add to your calendar:\n>> ')
                    date = input('Please enter the date in the format (MM/DD/YYYY):\n>> ')
                    # these conditions will raise a ValueError that must be handled and we will circle back to try again
                    if len(date) < 10 or len(date) > 10 or int(date[6:]) < int(strftime('%Y')):
                        raise ValueError
                    # if no information was entered incorrectly, the event will be added to the calendar here
                    else:
                        calendar[date] = event
                        print('Your event has been successfully added to your calendar.')
                        print(calendar)
                        # break out of the try/except protection loop
                        break
                # this will execute to handle the exception if the date raised a ValueError for meeting the error criteria
                except ValueError:
                    print('It seems your date entered was either incorrect or in the past. Please try again.')

        # delete from calendar
        elif user_choice == 'D':
            # no use deleting anything if the calendar is empty
            if len(calendar.keys()) < 1:
                print('The calendar is currently empty.')
            # get user input for desired event removal
            else:
                event = input('What event would you like to remove?\n>> ')
                # check if the event even exists
                if event in calendar.values():
                    # if event exists, loop through and remove the desired event
                    for k, v in list(calendar.items()):
                        if v != event:
                            continue
                        else:
                            del calendar[k]
                            print('The event has been successfully removed from your calendar.')
                            print(calendar)
                # skip the above if event doesn't exist, print a user notification
                else:
                    print('The event you specified doesn\'t exist or was incorrectly entered.')

            # message for input that doesn't match what was requested
        else:
            print('Please refrain from typing garbage as it will get you nowhere. You cannot escape without following instructions... Muahahahaha!')

# call the function to execute the script
if __name__ == '__main__':
    start_calendar()
