level1 = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

level2 = '''Some stuff on Command Line: This is another name for a folder: ___1___. This command will print your working directory: ___2___.
This command will list all of the files in your current directory: ___3___. This command will open your current directory or a specified file: ___4___.
This command will change your directory: ___5___. ___6___ creates a new file and ___7___ creates a new folder/directory. To execute a python file in
the terminal on Windows type ___8___ python filename.py'''

level3 = '''Debugging Strategy: 1. Examine error messages: the last line of Python ___1___ will tell you what went wrong.  2. Work from example code: ___2___
out your code and do step-by-step modifying to example code until it does what you want.  3. Make sure examples work  4.  Check (___3___) intermediate results.
When your code works(doesn't crash), but doesn't behave the way you expect, it can help to use ___3___ statements to see what is happening.  5. Keep & Compare
old versions: When you have a working version of you code ___4___ it before you add to it. This will give you something to go back to if you introduce too many
new ___5___.'''
placeholders = ["___1___", "___2___", "___3___", "___4___", "___5___", "___6___", "___7___", "___8___"]
answers = []
answers_level1 = ["function", "arguments", "None", "lists"]
answers_level2 = ["directory", "pwd", "ls", "start", "cd", "touch", "mkdir", "winpty"]
answers_level3 = ["tracebacks", "comment", "print", "save", "bugs"]
index = 0

# Starts the quiz and prompts the user for input
# Sets the answers list to the correct value based off the user input
# Sets the user's choice to the correct quiz which is used in the play_quiz function
def start_quiz():
    print "Please select a quiz level by typing it in."
    print "Possible choices include: 1, 2, 3"
    user_choice = select_difficulty()
    if user_choice == "1":
        user_choice = level1
        answers = answers_level1
    elif user_choice == "2":
        user_choice = level2
        answers = answers_level2
    else:
        user_choice = level3
        answers = answers_level3
    print user_choice + "\n"
    get_answers(user_choice, answers, index)

# Prompts the user to choose a difficulty for the quiz. Will prompt the user over and
# over again until they enter an acceptable input. Returns the user's difficulty choice.
def select_difficulty():
    difficulty_choices = ["1", "2", "3"]
    user_choice = raw_input()
    while user_choice not in difficulty_choices:
        print "Please choose 1, 2, or 3"
        user_choice = raw_input()
    print "You've chosen " + user_choice
    print ""
    print "You will get 5 guesses per problem"
    print ""
    return user_choice

#Asks the user what should be substitued in for the placeholder and gets their input as an answer.
#Takes the input of a string placeholder which is in the list of placeholders.
#Returns the user's answer.
def ask_question(placeholder):
    print "What should be substituted in for " + placeholder + "?"
    user_input = raw_input()
    return user_input

#Checks to see if the game is over.
#Takes an input number_of_guesses and tests to see if it is equal to zero.
#Returns True or False
def is_game_over(number_of_guesses):
    if number_of_guesses == 0:
        print "You ran out of turns! Better luck next time!"
        return True
    else:
        return False

#Updates the quiz question string when the user answers correctly.
#Takes 5 inputs: quiz_text - the quiz question, placeholder - the element of the placeholders list that is being searched for in q,
#the user's answer, the answers list, and an index to track location in the answers list
#Returns the updated string unless all answers have been answered the game ends.
def correct_answer(quiz_text, placeholder, user_answer, answers, index):
    index += 1
    quiz_text = quiz_text.replace(placeholder, user_answer)
    print "Correct!\n"
    if index == len(answers):
        print "You Win!!!"
        return quiz_text, index
    else:
        print quiz_text + "\n"
        return quiz_text, index

#Prints out that the user has answered the question incorrectly.
#Takes two inputs: quiz_text - the quiz question. guesses_left - the number of guesses remaining.
def wrong_answer(quiz_text, guesses_left):
    print "That isn't the correct answer! Let's try again. You have " + str(guesses_left) + " guesses left!"
    print "\n" + quiz_text + "\n"

#Gets the answers from the user, checks to see if they are right, and updates the quiz question as answers are provided. Ends game if user answers incorrectly too many times.
#Takes as an input quiz_text (a string that is the quiz question), answers (list of the answers for the selected play_quiz), and index which is initialized at zero
#Its only return is a value of None to end the game if the user has no guesses left
def get_answers(quiz_text, answers, index):
    for element in placeholders: #for every element in placeholders. i.e. ___1___, ___2___, and so on
        guesses_left = 5
        if quiz_text.find(element) > -1: #if the placeholder exists in the quiz question.
            user_answer = ask_question(placeholders[index])
            if user_answer == answers[index]:
                quiz_text, index = correct_answer(quiz_text, element, user_answer, answers, index)
            else:
                while guesses_left > 0:
                    guesses_left -= 1
                    if is_game_over(guesses_left):
                        return
                    wrong_answer(quiz_text, guesses_left)
                    user_answer = ask_question(placeholders[index])
                    if user_answer == answers[index]:
                        quiz_text, index = correct_answer(quiz_text, element, user_answer, answers, index)
                        break

start_quiz()
