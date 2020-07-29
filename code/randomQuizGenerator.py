#! python 3
### random quiz generator

import random

# data
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# generate 35 quiz files

for quizNum in range(35):

    # create quiz and answer key files
    qFile = open(f'.\docs\capitals_quiz\quiz{quizNum+1}.txt', 'w')
    aFile = open(f'.\docs\capitals_quiz\quiz_answer{quizNum+1}.txt', 'w')

    # write out header for quiz - for names and date
    qFile.write('Name:\nDate:\n\n')
    qFile.write((f'US Capitals Quiz - Form {quizNum+1}').center(50, '-'))
    qFile.write('\n\n')

    # shuffle order of states
    states = list(capitals.keys())
    random.shuffle(states)

    # loop through all 50 states, making a question each
    for i in range(50):

        # get right answer
        rightAns = capitals[states[i]]

        # get list of wrong answers to randomly select 3
        wrongAns = list(capitals.values())
        del wrongAns[wrongAns.index(rightAns)]
        wrongAns = random.sample(wrongAns, 3)
        ansOptions = wrongAns + [rightAns]

        # randomise right and 3 wrong answers to present
        random.shuffle(ansOptions)

        # write question and ans options to file
        qFile.write(f'Q{i+1}. What is the capital of {states[i]}?\n')
        for j in range(4):
            qFile.write(f"  {'ABCD'[j]}. {ansOptions[j]}\n")
        qFile.write('\n')

        # write answer key to file
        aFile.write(f"Q{i+1}. {'ABCD'[ansOptions.index(rightAns)]}\n")

    qFile.close()
    aFile.close()

        

        
