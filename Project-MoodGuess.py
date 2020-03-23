#mood guess!

#import module (random)
import random

#define a function called moodGuess with 1 parameter value of moodValue
def moodGuess(moodValue):

#based on the value of random.randint, returns one of the 9 moods
    if moodValue == 1:
        return 'You are happy?'
    elif moodValue == 2:
        return 'You are sleepy?'
    elif moodValue == 3:
        return 'You are shocked?'
    elif moodValue == 4:
        return 'You are hungry?'
    elif moodValue == 5:
        return 'You are sad?'
    elif moodValue == 6:
        return 'You are excited?'
    elif moodValue == 7:
        return 'You are proud?'
    elif moodValue == 8:
        return 'You are calm?'
    elif moodValue == 9:
        return 'You are lonely?'

#(result) variable is assigned to value of module (random)/function (randint)
#the function randint evaluates to a random value from 1 to 9. 
result = random.randint(1, 9)

#(mood) variable is assigned and called to function (moodGuess)
#the parameter of (moodValue) is now equal to (result) 
#based on the value evaluated from randint, determines the guess of mood.
mood = moodGuess(result)

#prints the mood guess.
print(mood) 
