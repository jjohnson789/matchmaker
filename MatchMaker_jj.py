# Jaylen Johnson
# Matchmaker 3000
# Credit to Eric Pogue

INTRODUCTION = '''
******************************************************
            Welcome to the Matchmaker 3000
          The Ultimate Compatability Test 
                    
               Presented by JayCorp
******************************************************

The goal of this program is to determine if we would be 
a suitible match.You will be presented with 5 different 
questions. For each question, you will choose from a range
of 5 down to 1. 5 means strongly agree, 4 is agree, 3 is 
neutral, 2 is disagree, and 1 is strongly disagree.

I hope you're my match made in heaven, good luck!

'''

QUESTION = [   
    'Spending time outdoors in nature is enjoyable.:',
    'The Seattle Seahawks are a great team!:',
    'Flying in an airplanes is scary.:',
     'On a scale of 1 to 5, how much do you enjoy Mac & Cheese?:',
     'I could never stand living in California.:'
]

DESIRED_RESPONSE = [ 
    5,
    5,
    1,
    5,
    1,
]

MAX_SCORE = 5* len(QUESTION)
print (INTRODUCTION)



response = []
compatability = []
for i in range(len(QUESTION)):
     userresponse = int(input(QUESTION[i]))
    
    
     response.append(userresponse)

     questioncompatability = 5 - abs(userresponse - DESIRED_RESPONSE [i])
     compatability.append(questioncompatability)

     print('Question %d Compatability: %d\n' % (i+1, questioncompatability))

totalcompatability = 0
for c in compatability:
    totalcompatability += c

totalcompatability *= 100 / MAX_SCORE
print('Total Compatibilty: %d\n\n' % (totalcompatability))

