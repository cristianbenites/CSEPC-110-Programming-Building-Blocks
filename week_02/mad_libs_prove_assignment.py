print("""
*************************************
*                                   *
*  Welcome to The Word Game \\O/     *
*  We will build a story together!! *
*                                   *
*************************************
""")

print('Please, answer the following questions:')

adjective = input('Write an adjective: ').lower()
animal = input('Animal: ').lower()
verb = input('A verb: ').lower()
exclamation = input('Exclamation: ').capitalize()
verb_2 = input('Another verb: ').lower()
verb_3 = input('Again, a new verb: ').lower()
adjective_2 = input('An adjective: ').lower()

print('\n\n----------------------------------')
print('Okay, this is our story:\n')

story = (
        f'The other day, I was really in trouble.\n'
        f'It all started when I saw a very {adjective} {animal} {verb} down the hallway.\n'
        f'"{exclamation}!" I yelled. But all I could think to do was to {verb_2} over and over.\n'
        f'Miraculously, that caused it to stop, but not before it tried to {verb_3} right in front of my family.\n'
        f'But the {adjective} {animal} didn\'t {verb_2} as good as me.\n'
        f'That moment was so {adjective_2}! I\'ll never forget it.'
    )

print(story)
