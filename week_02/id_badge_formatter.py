"""
Title: ID Badge Formatter
Author: Cristian Benites

Description: This program creates a properly formatted ID badge. 

Purpose: Practice formatting strings. 

This script also implements the stretch challanges.
"""

print("""
----------------------------------------
|
|   ID Badge Formatter
|
|   ,--------------.
|   | [] .~~~ ^^^^ |
|   | ^^^: ~~~~    |
|   | ~~# :; ^^~~~ |
|   \\______________/
|
----------------------------------------
""")
print("\nPlease enter the following information:\n")

# General required information
first_name = input("First name: ").title()
last_name = input("Last name: ").upper()
email_address = input("Email address: ").lower()
phone_number = input("Phone number: ").lower()
job_title = input("Job title: ").capitalize()
id_number = input("ID number: ")

# Strecht Activity information
hair_color = input("Your hair color: ").capitalize()
eye_color = input("Your eye color: ").capitalize()
initial_month = input("Write the name of the month you started (ex: June): ").capitalize()

# I used a y/n input because I think it will prevent users from inserting wrong answers.
# The script then checks if the result matches with 'Y' or if it's empty (default option).
# However, I think that regex would be better to avoid several if else checks.
# I'll make that improvement in further activities
completed_advanced_training = input("Have you completed the advanced training? (Y/n) ")
completed_advanced_training = "Yes" if completed_advanced_training.upper() == "Y" or not completed_advanced_training else "No"

# For multiple line prompts I'm a big fan of triple quotes strings, that's why I chose that approach
# Prior to this activity, I didn't know how to accomplish the spacing, so I
# found this way.

print("\n\nThe ID Card is:")
print(f"""
 -----------------------------------------
  {last_name}, {first_name}
  {job_title}
  ID: {id_number}
  
  {email_address}
  {phone_number}
  
  {'Hair: ' + hair_color: <20} Eyes: {eye_color}
  {'Month: ' + initial_month: <20} Training: {completed_advanced_training}
 -----------------------------------------
""")
