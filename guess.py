import random

guessesTaken = 0

print('Привет! Как тебя зовут?')

myName = input()

number = random.randint(1, 10)
print('Что ж, ' + myName + ', я загадываю число от 1 до 20.')

for guessesTaken in range(3):
    print('Попробуй угадать.')
    guess = int(input('Введи число \n'))

    if guess < number:
        print('Твоё число слишком мало.')
    elif guess > number:
        print('Твоё число слишком велико')
    elif guess == number:
        print('Поздравляю,' + myName + ', ты угадал за' + str(guessesTaken + 1) + 'попытки')
        break
if guess!= number:
    print('Загаданное число было ' + str(number))