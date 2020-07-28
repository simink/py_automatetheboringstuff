## Multiplication quiz

import pyinputplus as pyip
import random, time

numberOfQuestions = 3
correctAnswers = 0
for questionNumber in range(numberOfQuestions):
    # pick two random numbers
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)

    prompt = '#%s: %s x %s = ' % (questionNumber+1, num1, num2)

    try:
        # right answers handled by allowRegexes
        # wrong answers handled by blockRegexes
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)], blockRegexes=[('.*', 'Incorrect!')], timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
        
    else:
        # this block runs if no exception were raised in the try block
        print('Correct')
        correctAnswers += 1
    
        time.sleep(1)  # brief pause to let user see result

    print('Score: %s / %s' % (correctAnswers, numberOfQuestions))

        