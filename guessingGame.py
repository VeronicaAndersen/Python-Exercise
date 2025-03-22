import random 

def computerGuess(lowval, highval, randnum, count = 0):
    if highval >= lowval:
        guess = lowval + (highval - lowval) // 2
        if guess == randnum:
            return count

        elif guess > randnum:
            count = count + 1
            return computerGuess(lowval, guess-1, randnum, count)

        else:
            count = count + 1
            return computerGuess(guess + 1, highval, randnum, count)
    else:
        return -1
#end of function

randnum = random.randint(1,100)

count = 0
guess = -99

while (guess != randnum):
    # Get the user's guess
    guess = (int) (input('Enter your guess between 1 - 100: '))
    if (guess < randnum):
        print('Higher')
    elif guess > randnum:
        print('Lower')
    else:
        print('Congrats')   
        break
    count = count + 1
#end of while loop

print('You took', str(count), 'steps to guess the number')
print('Computer took', str(computerGuess(0,100, randnum)), 'steps')