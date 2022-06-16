from time import sleep

welcome_message = '''
* * * * * * * * * * * * * * * * * * * * * * * * * *
*                                                 *
*  Welcome to The Interviewer!                    *
*  We'll now ask you a few questions to meet you  *
*                                                 *
* * * * * * * * * * * * * * * * * * * * * * * * * *
'''
print(welcome_message)
sleep(2)

name = input('What is your name? \n')
if name:
    age_question = f"Alright, {name}, nice to meet you.\nWhat is your age?\n" 
else:
    name = "My Friend"
    age_question = f"Ok! So I will call you {name}.\nWhat is your age? (in years)\n"

age = input(age_question)

favorite_color = input(f"What is your favorite color, {name}? \n")

final_message = f'''
* * * * * * * * * * * * * * * * * * * * * * * * * *
                                                  
   This is {name}, {age} years old.               
   {name}'s favorite color is {favorite_color}                                                 
 
* * * * * * * * * * * * * * * * * * * * * * * * * *
'''

print(final_message)
