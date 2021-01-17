import random



print('Welcome to the number guessing game\nI am thinking of a different number betweeen 1 and 100')
print('You have 5 guesses')
numbers=[i for i in range(0,101,1)]

goal=random.choice(numbers)

mode=input('Choose a difficulty,type "easy" for easy and "hard" for hard\n')
if mode=='easy':
 number_of_guesses=10
 print(f'You are given {number_of_guesses} attempts to find the number')
elif mode=='hard':
 number_of_guesses = 5
 print(f'You are given {number_of_guesses} attempts to find the number')
found=False

while number_of_guesses>0 and found==False:
    guess = int(input('Make a guess:'))
    if guess>goal:
        number_of_guesses-=1
        if number_of_guesses!=0:
         print(f'Your guess is too high, you have {number_of_guesses} attempts left')
    elif goal>guess:
        number_of_guesses -= 1
        if number_of_guesses != 0:
         print(f'Your guess is too low, you have {number_of_guesses} attempts left')
    elif goal==guess:
        print('You found it!')
        found=True


if found==False:
    print(f'You lost, the number I am thinking is {goal}')



