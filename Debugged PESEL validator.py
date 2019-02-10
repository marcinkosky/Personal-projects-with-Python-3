#!/usr/bin/env python
from datetime import date

print("PESEL number verification. Version 4.4\nType your PESEL number below:")
pesel_input = '90030616517'
(month, day) = (0, 0)

days_count = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
              7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


def beginning(n):
    pesel_len = len(str(n))
    pesel_diff = abs(pesel_len - 11)
    global pesel_input_validation, month, day, year_count
    if pesel_input.isnumeric() is True:
        if pesel_len == 11:
            pesel_input_validation = True
            s = [int(i) for i in n]
            pesel_control_sum = 9 * int(s[0]) + 7 * int(s[1]) + 3 * int(s[2]) \
                + 1 * int(s[3]) + 9 * int(s[4]) + 7 * int(n[5]) + 3 *int(s[6])\
                + 1 * int(s[7]) + 9 * int(s[8]) + 7 * int(s[9])
            if pesel_control_sum % 10 == int(s[10]):
                print("\nYour PESEL number {} is correct.".format(pesel_input))
                (year, month) = (int(pesel_input[0:2]), int(pesel_input[2:4]))
                month_index = int(pesel_input[2])
                day = int(pesel_input[4:6])
                if (month_index == 0) or (month_index == 1):
                    year_prefix = 19
                elif (month_index == 2) or (month_index == 3):
                    year_prefix = 20
                    month -= 20
                elif (month_index == 4) or (month_index == 5):
                    year_prefix = 21
                    month -= 40
                elif (month_index == 6) or (month_index == 7):
                    year_prefix = 22
                    month -= 60
                elif (month_index == 8) or (month_index == 9):
                    year_prefix = 18
                    month -= 80
                year_count = year_prefix * 100 + year
                pesel_input_validation = True
            else:
                pesel_input_validation = False
        elif pesel_len < 11:
            print("\nYour PESEL number is too short.")
            print("You've wrote {} out of {} PESEL digits. {} digits to fill."
            .format(pesel_len, 11, pesel_diff))
            pesel_input_validation = False
        elif pesel_len > 11:
            print("\nYour PESEL number is too long.")
            print("You've wrote {} out of {} PESEL digits. {} digits too much."
            .format(pesel_len, 11, pesel_diff))
            pesel_input_validation = False
        else:
            pesel_input_validation = False
    else:
        print("\nYour PESEL number '{}' is incorrect.".format(pesel_input))
        pesel_input_validation = False


def leap_year(n):
        if (year_count % 4 == 0) and (year_count % 100 != 0) or (year_count % 400 == 0):
            days_count[2] = 29


def birth_date(month, day):
    global date_input_validation
    max_days = days_count.get(month)
    if (max_days is not None) and (day <= max_days):
        print("\a Your birth date is {}-{}-{}."
            .format(day, month, year_count))
        date_input_validation = True
    else:
        print("Error, invalid date. You can't be born on {}-{}-{}."
            .format(day, month, year_count))
        date_input_validation = False


def pesel_input_sex(n):
    if n[9] in '02468':
        print("\a You are a female.")
    else:
        print("\a You are a male.")


def pesel_age(n):
    current_year = int(date.today().year)
    print("\a You are {} years old.".format(current_year - year_count))

beginning(pesel_input)

if pesel_input_validation:
    leap_year(pesel_input)
    birth_date(month, day)
    if date_input_validation:
        pesel_input_sex(pesel_input)
        pesel_age(pesel_input)
