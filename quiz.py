""" 
Quiz 

Questions, answer, options
correct answer
print total question, count of correct answer, count of wrong answers 
 """


questions = [
    {   
        "question" : "How to write for loop? ",
        "options" : ["A: for i in item", "B: for i -> Item", "C: for items"], 
        "answer" : "A"
    },
    {
        "question" : "How to write function? ", 
        "options" : ["A: function_name", "B: def functionName()", "C: def function name()"], 
        "answer" : "B"
    },
    {
        "question" : "How to write dict? ", 
        "options" : ["A: define only values", "B: define only keys", "C: define key value pair"], 
        "answer" : "C"
    },
]

correctAnswersList = []

def startGame():
    print("Game Start")
    for question in questions:
        print('---------------------')
        print(question['question'])

        for option in question['options']:
            print(option)

        guess = input("Select your Option: ")
        guess = guess.upper()

        if guess == question['answer']:
            correctAnswersList.append(question)

    
def results():
    questionListCount = len(questions)
    correctAnswersListCount = len(correctAnswersList)
    wrongAnswers = questionListCount - correctAnswersListCount
    
    print("Total questions: {}".format(questionListCount))
    print("Correct Answers: {}".format(correctAnswersListCount))
    print("Wrong Answers : {}".format(wrongAnswers))


startGame()
results()