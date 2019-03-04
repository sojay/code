""" This program should enable the user to choose to view the calendar, add an event to the calendar, update an existing event, delete an existing event! """
from time import sleep, strftime
import sys
user_first_name = "Samuel"
calendar = {}


def welcome():
    print "Welcome, " + user_first_name + "."
    print "Calendar is opening..."
    sleep(1)
    print "Today's date is: " + strftime("%A %B %d, %Y")
    print "The time is: " + strftime("%H: %M: %S")
    sleep(1)
    print "What would you like to do?"


def start_calendar():
    welcome()
    start = True
    while start:
        user_choice = raw_input("Choose A to Add, U to Update, V to view, D to Delete, X to Exit: ")
        user_choice = user_choice.upper()
        if user_choice == 'V':
            if len(calendar.keys()) < 1:
                print "Your calendar is free"
            else:
                print calendar
        elif user_choice == 'U':
            date = raw_input("What date?")
            update = raw_input("Enter the update: ")
            update = update.upper()
            calendar[date] = update
            print "Update successful!"
            print calendar
        elif user_choice == 'A':
            event = raw_input("Enter event: ")
            event = event.upper()
            date = raw_input("Enter date (MM/DD/YYYY): ")
            date = date.upper()
            if (len(date) > 10 or int(date[6:]) < int(strftime("%Y"))):
                print "Invalid date"
                try_again = raw_input("Try Again? Y for Yes, N for No: ")
                try_again.upper()
                if try_again == "Y":
                    continue
                else:
                    start = False
            else:
                calendar[date] = event
                print "Event successfully added"
        elif user_choice == "D":
            if len(calendar.keys()) < 0:
                print "Calendar is empty"
            else:
                event = raw_input("What event?: ")
                for date in calendar.keys():
                  if event == calendar[date]:
                    del calendar[date]
                    print "Event successfuly deleted"
                else:
                    print "Incorrect date"
        elif user_choice == "X":
          sys.exit()
        else:
          print "Invalid Command"
          print "Calendar is exiting..."
      
start_calendar()