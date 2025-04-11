# Set the variables
user_name = input("What is your name? ")
print("Hello {}".format(user_name))
score = 0

# List the questions
Question_list = [\
'Q1: When did \"A Minecraft movie\" come out?\n A: 3rd of April\n B: 4th of April\n C: 1st of April\n',\
'Q2: Who plays the character Steve?\n',\
'Q3: What did \"Steve\" want as a kid?\n" A: To mine.\n B: To work.\n C: live wit his parents\n.']

Answer_list = ['A','Jack Black','A']

# Make the questions
answer = input(Question_list[0])
if answer == Answer_list[0]:
    score += 10
    print ("Good job\nYour new score is {}\n".format(score))
else:
    print ("Sorry, thats wrong\n your score will stay the same")

# "Q1: When did \"A Minecraft movie\" come out?\n A: 3rd of April\n B: 4th of April\n C: 1st of April/n

# "Q2: Who plays the character Steve?\n") 
# Jack black

# "Q3: What did \"Steve\" want as a kid?\n" A: To mine.\n B: To work.\n C: live wit his parents\n.

# "Q4: Finish the line \"Flint and _____\"\n"
# Steel.

# "Q5: Finish the line \"_____ bucket release\"\n" 
# Water.

# "Q6: What is the name of the movie \"A Minecraft movie\"?\n" 
# A Minecraft movie
