#!/usr/bin/env python

print("""Welcome to the Least common multiple (LCM).
Program is running with methods and functions by using formula:
LCM(A, B) = A * B / GCD(A, B)\n""")

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

print(f'LCM({first_int}, {second_int}) = {first_int} * {second_int} / GCD({first_int} / {second_int})')
print(f'LCM({first_int}, {second_int}) = {first_int * second_int} / {gcd(first_int, second_int)}')
print(f'LCM({first_int}, {second_int}) = {first_int * second_int / gcd(first_int, second_int)}')
