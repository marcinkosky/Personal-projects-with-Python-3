#!/usr/bin/env python

print("""Welcome to the Greatest common divisor finder (GCD).
Program is running with methods and functions, without euclid_algo()
Please type two numbers, greater than zero.\n""")

int_list = []

while True:
    try:
        first_int = int(input('Enter the first number:'))
        break
    except ValueError:
        print('Invalid input. Please try again:\n')

while True:
    try:
        second_int = int(input('Enter the second number:'))
        break
    except ValueError:
        print('Invalid input. Please try again:\n')

print()

if second_int > first_int:
    first_int, second_int = second_int, first_int


def gcd(a, b):
    if a == 0:
        return b
    int_list.append(a)
    return gcd(b % a, a)


gcd(first_int, second_int)

for i in range(len(int_list) - 1):
    print(
        f'{int_list[i]} : {int_list[i + 1]} = {int_list[i] // int_list[i + 1]} \
| rest is {int_list[i] % int_list[i + 1]}')

print(f'\nGCD for {first_int} and {second_int} is number {min(int_list)}.')
