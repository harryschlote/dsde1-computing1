message = 'Hello, time to play a guessing game!'
print( message )
print( )
print('Firstly, what is your name?')
player_name = input()
print('Hello ' + str(player_name) + ',exit() lets play the game!')
print("Guess a number between 1 and 10")
guess_number = input()

print( 'you guessed ' + guess_number )
import random
correct_number = random.randint(1,10)
print('the actual number is ' + str(correct_number) )
print('your number is ' + str(correct_number == guess_number))
print('Did you get it correct?')
input()
print()
print()
print('That is a shame!')
print( 'Goodbye')
print()
print()
print()
print('Only joking, you can have another guess!')
print('Enter another number (p.s. the random number will change!)')
guess_number2 = input()

print( 'you guessed ' + guess_number2 )
import random
correct_number2 = random.randint(1,10)
print('the actual number is ' + str(correct_number2) )
print('your number is ' + str(correct_number2 == guess_number2))
print('Did you get it correct?')
input()
print('That is a shame!')
print( 'Goodbye')