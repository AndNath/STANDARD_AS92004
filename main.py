# Set the variables
score = 0

# Lists of the questions & answers
Question_list = [\
'Q1: When did \"A Minecraft movie\" come out?\n A: 4rd of April\n B: 3th of April\n C: 1st of April\n',\
'Q2: Who plays the character Steve?\n',\
'Q3: What did \"Steve\" want as a kid?\n A: To mine.\n B: To work.\n C: live with his parents.\n',\
'Q4: Finish the line \"Flint and _____\"\n',\
'Q5: Finish the line \"_____ bucket release\"\n',\
'Q6: What is the name of the movie \"A Minecraft movie\"?\n',\
'Q7: Where was \"A Minecraft Movie\" filmed?\n ']

Answer_list = ['b','jack black','a','steel','water','a minecraft movie','new zealand']

# Displays the questions to the user
for i in range(len(Question_list)): # Repeats until it cant anymore
    answer = input(Question_list[i])
    if answer.lower() == Answer_list[i].lower():
        score += 10
        print("Good job\nYour new score is {}\n".format(score))
    else:
        print("Sorry, that's wrong\nYour score will stay at {}\n".format(score))
# Ending statement
print("Your final score is {}/70".format(score))
print("Thank you for playing my quiz about \"A Minecraft Movie\"\nI hope you enjoyed it")
