#!/usr/bin/env python3

# Created by: Peter Sobowale
# Created on: Jan 2, 2023
# This program uses a while loop to collect input
# from the user. It then calls a function calculate
# the average of the input.
import math


# function calculates the average in the list of elements
def calc_average(marks):
    median = 0

    for counter in range(len(marks)):
        median += marks[counter]

    if len(marks) == 0:
        return -1
    else:
        median = median / len(marks)
        return median


# get input from user and checks for invalid input
def main():

    # declaring variable
    marks_list = []
    temp_mark = None

    # user interface
    print("This program will calculate the average of all the user's marks.\n")

    # gets input from user and adds it to end of list
    while temp_mark != "-1":
        temp_mark = input("Enter a mark between 0 and 100 (-1 to stop): ")
        try:
            mark_int = int(temp_mark)
            if mark_int == -1:
                continue
            elif mark_int < 0 or mark_int > 100:
                print(f"{mark_int} is not between 0 and 100.")
                continue
            marks_list.append(mark_int)
        except Exception:
            print(f"{temp_mark} is not a valid mark.")
            continue

    # assigns variable to function call
    average_user = calc_average(marks_list)
    average_user = round(average_user)

    # displays results to user
    print("\nFor the list of marks: {}".format(marks_list))
    print("The average is {}%".format(average_user))


if __name__ == "__main__":
    main()
