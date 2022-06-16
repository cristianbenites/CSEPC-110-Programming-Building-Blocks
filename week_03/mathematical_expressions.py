"""
File: w03_prepare_numeric_data_types.py
Author: Cristian Benites

Purpose: Practice using mathematical expressions.
"""

age = int(input('How old are you? '))

print(f'On your next birthday you, will be {age + 1} years old')

egg_cartons = int(input('how many egg cartons do you have? '))

print(f'You have {egg_cartons * 12} eggs')

number_of_cookies = int(input('How many cookies do you have? '))
number_of_people = int(input('How many people are there? '))

if number_of_people == 0:
    print(f'The number of people can\'t be zero (impossible to divide by 0)')
    exit()

amount = number_of_cookies / number_of_people
cookies = 'cookie' if amount == 1 else 'cookies'

print(f'Each person may have { amount } {cookies}')
