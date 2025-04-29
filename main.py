# Variables & Time
score = 0
import time

# Intro to the quiz
print("Welcome to the \"A Minecraft Movie\" quiz.\nI hope you have fun playing.\n")
time.sleep(2)
# Lists of the questions & answers
Question_list = [\
'Q1: When did \"A Minecraft movie\" come out?\n A: 4rd of April\n B: 3th of April\n C: 1st of April\n ',\
'Q2: Who plays the character Steve?\n ',\
'Q3: What did \"Steve\" want as a kid?\n A: To mine.\n B: To work.\n C: live with his parents.\n ',\
'Q4: Finish the line, \"Flint and _____\"\n ',\
'Q5: Finish the line \"_____ bucket release\"\n ',\
'Q6: What is the name of the movie \"A Minecraft movie\"?\n ',\
'Q7: Where was \"A Minecraft Movie\" filmed?\n ']

Answer_list = ['b','jack black','a','steel','water','a minecraft movie','new zealand']

# Displays the questions to the user
for i in range(len(Question_list)): # Repeats until it cant anymore
    answer = input(Question_list[i])
    if answer.lower() == Answer_list[i].lower():
        score += 10
        print("\nGood job\nYour new score is {}\n".format(score))
        time.sleep(1.5)
    else:
        print("\nSorry, that's wrong\nYour score will stay at {}\n".format(score))
        time.sleep(1.5)

# Outro & final score
print("Your final score is {}/70".format(score))
print("Thank you for playing my quiz about \"A Minecraft Movie\"\nI hope you enjoyed it")
