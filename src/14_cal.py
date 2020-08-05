"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

tc = calendar.TextCalendar(firstweekday=0)

d = datetime.now()

y = d.year

m = d.month

args = sys.argv

def cal(args):
  args_len = len(args)
  if (args_len == 1):
    print(tc.formatmonth(d.year, d.month))
  elif (args_len == 2):
    if (len(args[1]) == 4 and int(args[1]) < 2020):
      print(tc.formatmonth(int(args[1]), d.month))
    else:
      print(sys.argv[0])
  elif (args_len == 3):
    if (((len(args[1]) < 3) and (int(args[1]) < 13)) and (len(args[2]) == 4 and int(args[2]) < 2020)):
      print(tc.formatmonth(int(args[2]), int(args[1])))
    else:
      print("This file expects input with the format of 'mm yyyy' or 'yyyy'.")

cal(sys.argv)