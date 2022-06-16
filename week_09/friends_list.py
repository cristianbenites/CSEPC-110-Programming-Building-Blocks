friends = []

user_answer = ''
while user_answer != 'end':
    user_answer = input("Type the name of a friend: ")

    if user_answer != 'end':
        friends.append(user_answer)

print('Your friends are:')

for friend in friends: print(friend)
