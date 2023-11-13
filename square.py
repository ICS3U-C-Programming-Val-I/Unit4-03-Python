#!/usr/bin/env python3

# Created By: Val Ijaola
# Date: November 12, 2023
# This program asks the user to enter a positive number.
# Then it tells them the square of the number.


def main():
    # getting number from user.
    num_str = input("Enter a number: ")
    power = 1

    try:
        # process - try catch and calculate square.
        num_int = int(num_str)

        if num_int < 0:
            print("Enter a non-negative number")
        elif num_int == 0:
            print("0^2 = 1")
        else:
            for counter in range(1, num_int + 1):
                power = counter**2
                print(f"{counter}^2 = {power}")
    except ValueError:
        print(f"{num_str} is not a number")


if __name__ == "__main__":
    main()
