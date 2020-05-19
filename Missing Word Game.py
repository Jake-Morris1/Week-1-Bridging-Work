# Fill in the missing word game
# 19-05-2020
# Jake Morris

fileName="Quotes.txt"
fileData=open(fileName, "r")
fullFile=fileData.readlines()
score=0

input("I am going to say some quotes from films but one word is blanked out. Guess that word. Press ENTER to continue. ")
print()

# Question 1
quote1=(fullFile[0]).replace("<force>", "_____")
question=input(quote1).lower()

if question=="force":
    print("Correct \n")
    score=score+1
else:
    print("Incorrect")
    print(fullFile[1], "\n")

# Question 2
quote1=(fullFile[2]).replace("<home>", "_____")
question=input(quote1).lower()

if question=="home":
    print("Correct \n")
    score=score+1
else:
    print("Incorrect")
    print(fullFile[3], "\n")

# Question 3
quote1=(fullFile[4]).replace("<chocolates>", "_____")
question=input(quote1).lower()

if question=="chocolates":
    print("Correct \n")
    score=score+1
else:
    print("Incorrect")
    print(fullFile[5], "\n")

# Question 4
quote1=(fullFile[6]).replace("<Housten>", "_____")
question=input(quote1).lower()

if question=="housten":
    print("Correct \n")
    score=score+1
else:
    print("Incorrect")
    print(fullFile[7], "\n")

# Question 5
quote1=(fullFile[8]).replace("<roads>", "_____")
question=input(quote1).lower()

if question=="roads":
    print("Correct \n")
    score=score+1
else:
    print("Incorrect")
    print(fullFile[9], "\n")

# Question 6
quote1=(fullFile[10]).replace("<infinity>", "_____")
question=input(quote1).lower()

if question=="infinity":
    print("Correct \n")
    score=score+1
else:
    print("Incorrect")
    print(fullFile[11], "\n")
fileData.close()

print("Thanks for playing!")
print("Your score is", score, " out of 6.")
name=input("Enter your name. ")

score=str(score)
fileName="Quotes Quiz Scores.txt"
fileData=open(fileName, "a")

fileData.writelines(name)
fileData.writelines("\n")
fileData.writelines(score)
fileData.writelines("\n")
fileData.writelines("\n")
fileData.close()





    




