#
# DATA
#
difficulty_levels = ["0", "1", "2", "3", "4", "5", "6"]

# QUESTIONS USED IN THE QUIZ
question_easy = "____1____ are placeholders for the values they are \
substituting. An assignment statement uses an ____2____ sign to assign a \
value to the variable. A variable's value can ____3____ with another \
____4____ statement. \n"

question_medium = "A string is a sequence of ____1____ that are surrounded with \
single/double quotes. Without the quotes it would be just a ____2____. \
The first character of the string is indexed as ____3____. \
Use the ____4____ sign to concatenate strings. \n"

question_hard = "A functions starts with a ____1____ keyword. \
The function name is followed by ____2____s (if any) surrounded by \
parentheses. Functions are useful because they can perform tasks that \
____3____ with no sweat. The last statement of a function is a ____4____ \
statement. ____5____ variables are variables defined inside the function. \n"

question_evil = "Grace Hopper was born in December 9 , 1906 and died in \
January 1, 1992. She was a United States Navy Rear Admiral. She was also a \
computer scientist who helped to invent ____1____, one of the first \
high-level programming languages, shattering the belief that computers could \
only do ____2____ tasks. She was known to carry ____3____ which were strings \
of copper wire that were the length that the speed of light could travel \
in one ____4____. \n"

questions = [question_easy, question_medium, question_hard, question_evil]

# ANSWERS TO QUESTIONS USED IN THE QUIZ
answers_easy = ["Variables", "=", "change", "assignment"]
answers_medium = ["characters", "variable", "0", "+"]
answers_hard = ["def", "parameters", "repeat", "return", "Local"]
answers_evil = ["COBOL", "arithmetic", "nanosticks", "nanosecond"]

answers = [answers_easy, answers_medium, answers_hard, answers_evil]


def get_level():
    """
    get user input of difficulty level
    :param: None
    :return: quiz_level
    """
    level = raw_input("Select difficulty: 1:easy 2:medium 3:hard 4:evil \
    \nor press 0 to exit \n")

    if level in difficulty_levels:
        quiz_level = int(level)
    else:
        quiz_level = 0
    return quiz_level


def replace_substring(target_string, substring, new_substring):
    """
    replaces substring with new_substring in the target_string
    :param target_string
    :param substring
    :param new_substring: new substring to replace
    :return: target_string updated with new_substring
    """
    replaced = []
    list_of_words = target_string.split()
    for word in list_of_words:
        if substring in word:
            word = word.replace(substring, new_substring)
        replaced.append(word)
    return " ".join(replaced)


def play_quiz(all_questions, all_answers):
    """This program implements the Reverse Mad-Libs game which
       prompts the player to fill in the blanks of quiz questions.
       1 - There can be up to 6 difficulties in the quiz.
       2 - All blanks have to be in the format ___n___ where n is
           a blank number surrounded by 4 underscores.
       3 - There can be up to 9 questions in each quiz level only.
       :param all_questions
       :param all_answers
       :return None"""
    # Greeting!
    raw_input("Hello player! Welcome to the quiz!! Press enter." + "\n")

    quiz_level = 1
    while quiz_level != 0:
        quiz_level = get_level()
        if quiz_level == 0:
            print "Good bye"                # Display if user quits
        else:
            # Displays questions
            question = all_questions[quiz_level - 1]

            # Loop through all questions
            for index in range(0, len(all_answers[quiz_level-1])):
                print question

                # Loop until answer is correct
                while raw_input("What should go in blank #" +
                                str(index + 1) + "? ").lower() != \
                        all_answers[quiz_level - 1][index].lower():
                    print "Wrong answer, Please try again!\n"

                # Display updated question set
                print "\nCorrect! Let's continue. \n"
                question = replace_substring(question,
                                             "____" + str(index + 1) + "____",
                                             all_answers[quiz_level-1][index])

            # Display after all questions answered correctly
            print "\nCongrats!!! Let's play more! \n"

# MAIN CODE: LET'S PLAY THE GAME
if __name__ == "__main__":
    play_quiz(questions, answers)
