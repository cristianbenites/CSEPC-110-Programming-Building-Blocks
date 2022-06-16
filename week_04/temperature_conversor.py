"""
Title: Temperature Conversor
Author: Cristian Benites

Description: This program makes the proper conversion from Farenheit to Celsius. 

"""

def convert(value_farenheit):
    return (value_farenheit - 32) * (5 / 9)

value_farenheit = float(input('What is the temperature in Farenheit? '))
value_celsius = convert(value_farenheit)

print(f'{value_farenheit:.1f} Farenheit is equivalent to {value_celsius:.1f} Celsius')

    
