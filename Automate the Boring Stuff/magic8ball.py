# Simulates a Magic 8 Ball
import random as rand

# Function used to shake the Magic 8 Ball
def shakeBall(messages):
    print('\nThe ball says...')
    print('\t' + messages[rand.randint(0, len(messages) - 1)] + '\n')

messages = [
    'It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']

print('=======================================================================================')
print('Welcome to the digital Magic 8 Ball. Press \'s\' to shake the ball, or \'q\' to quit.')
print('=======================================================================================')

play = input().lower()

while play != 'q':
    if play == 's':
        shakeBall(messages)
        print('Press \'s\' to shake again, or \'q\' to quit.')
        play = input().lower()
    else:
        print('Invalid input. Press \'s\' to shake, or \'q\' to quit.')

# When the user enters 'q' to quit the game
print('Thank you for playing! Have a nice day.')





