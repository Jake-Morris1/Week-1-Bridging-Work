# Maths quiz
# 18-05-20
# Jake Morris

import random

easyQuestions=["12 + __ = 15 ", "__ - 22 = -8 ", "54 / 6 = __ ", "13 * __ = 26 ", "__ + 4 = 29 ", "20 - __ = 3 ", "30 / __ = 2 ", "23 * 0 = __ ", "28 + 9 = __ ", "1 - 10 = __ " ," __ / 9 = 2 ", "__ * 3 = 36 "]
easyAnswers=[3, 14, 9, 2, 25, 17, 15, 0, 37, -9, 18, 12]

mediumQuestions=["__ + 9 + 5 = 22", "42 + __ + 33 = 115 ", "__ - 14 + 12 = 46", "46 + 21 - 7 = __ ", "25 - 11 * 2 = __ ", "6 * __ + 22 = 46 ", "29 + 16 / __ = 33 ", "__ - 26 / 1 = 39", "2 * 7 * 4 = __ ", "__ * 4 / 2 = 6 ", "100 / __ * 7 = 70 ", "6 / 2 / __ = 3 ", "16 / 4 / 2 = __ "]
mediumAnswers=[8, 40, 20, 60, 3, 4, 4, 62, 56, 10, 1, 2]

hardQuestions=["-13 + 25 + __ = 13 ", "5 / 2 + 3.2 = __ ", "8.4 + __ + 13.23 = 26.32 ", " -1.2 * 4 - __ = 1 ", "1 / __ * 3 = 1.5 ", "5.4 - 4.1 + 17.8 = __ ", "__ + 4.7 - 9.4 = 34.2 ", "4.32 - 10 + __ = -2.78 ", "20.13 - 8.4 * __ = 0 ", "9.8 - 10 + __ = 12 " ,"1 / 3 * 6 = __ ","8.5 - __ + 5.04 = 45.14 "]
hardAnswers=[1, 5.7, 4.35, 1.3, 2, 19.1, 20.1, 2.9, 0, -12.2, 2, 31.6]

askedQuestions=[]
askedAnswers=[]
indexList=[]
score=0


def easyMode():
    counter=0
    while counter <= 3:
        index=random.randint(0,12)   # Chooses a number at random to use as an index

        if index not in indexList: # Checking that a question isn't picked twice on the same round

            indexList.append(index)
            quest=easyQuestions[index]
            askedQuestions.append(quest)  # Putting a random question into a list
            ans=easyAnswers[index]
            askedAnswers.append(ans)      #Putting a random answer that matches with the question into a list
            counter=counter+1
            
        
    question1=float(input(askedQuestions[0]))  # Gets the question from the list
    question1ans=askedAnswers[0]             # Gets the answers that's linked to the question
    if question1 == question1ans:
        score=score+1
        print("Correct")
    else:
        print("Incorrect")
        
    question2=float(input(askedQuestions[1]))  
    question2ans=askedAnswers[1]             
    if question2 == question2ans:
        score=score+1
        print("Correct")
    else:
        print("Incorrect")

    question3=float(input(askedQuestions[2]))  
    question3ans=askedAnswers[2]             
    if question3 == question3ans:
        score=score+1
        print("Correct")
    else:
        print("Incorrect")

    print("Your score is", score, "out of 3. ")
    name=input("Enter your name. ")
    score=str(score)
    # Puts the score onto a text file
    fileName="Maths Quiz - Easy.txt"
    fileData=open(fileName, "a")
    fileData.writelines(name)
    fileData.writelines("\n")
    fileData.writelines(score)
    fileData.writelines("\n")
    fileData.writelines("\n")
    fileData.close()



def mediumMode():
    counter=0
    while counter <= 3:
        index=random.randint(0,12)   

        if index not in indexList: 

            indexList.append(index)
            quest=mediumQuestions[index]
            askedQuestions.append(quest)  
            ans=mediumAnswers[index]
            askedAnswers.append(ans)      
            counter=counter+1
            
        
    question1=float(input(askedQuestions[0]))  
    question1ans=askedAnswers[0]             
    if question1 == question1ans:
        score=score+1
        print("Correct")
    else:
        print("Incorrect")
        
    question2=float(input(askedQuestions[1]))  
    question2ans=askedAnswers[1]             
    if question2 == question2ans:
        score=score+1
        print("Correct")
    else:
        print("Incorrect")

    question3=float(input(askedQuestions[2]))  
    question3ans=askedAnswers[2]             
    if question3 == question3ans:
        score=score+1
        print("Correct")
    else:
        print("Incorrect")

    print("Your score is", score, "out of 3. ")
    name=input("Enter your name. ")
    score=str(score)
    
    fileName="Maths Quiz - Medium.txt"
    fileData=open(fileName, "a")
    fileData.writelines(name)
    fileData.writelines("\n")
    fileData.writelines(score)
    fileData.writelines("\n")
    fileData.writelines("\n")
    fileData.close()



def hardMode():
    counter=0
    while counter <= 3:
        index=random.randint(0,12)   

        if index not in indexList: 

            indexList.append(index)
            quest=hardQuestions[index]
            askedQuestions.append(quest)  
            ans=hardAnswers[index]
            askedAnswers.append(ans)      
            counter=counter+1
            
        
    question1=float(input(askedQuestions[0]))  
    question1ans=askedAnswers[0]             
    if question1 == question1ans:
        score=score+1
        print("Correct")
    else:
        print("Incorrect")
        
    question2=float(input(askedQuestions[1]))  
    question2ans=askedAnswers[1]             
    if question2 == question2ans:
        score=score+1
        print("Correct")
    else:
        print("Incorrect")

    question3=float(input(askedQuestions[2]))  
    question3ans=askedAnswers[2]             
    if question3 == question3ans:
        score=score+1
        print("Correct")
    else:
        print("Incorrect")

    print("Your score is", score, "out of 3. ")
    name=input("Enter your name. ")
    score=str(score)
    
    fileName="Maths Quiz - Hard.txt"
    fileData=open(fileName, "a")
    fileData.writelines(name)
    fileData.writelines("\n")
    fileData.writelines(score)
    fileData.writelines("\n")
    fileData.writelines("\n")
    fileData.close()





difficulty=""
while difficulty != "easy" and difficulty!="medium" and difficulty!="hard":
    difficulty = input("Enter your difficulty. Easy, Medium, Hard. ")
    difficulty = difficulty.lower()
    if difficulty != "easy" and difficulty!="medium" and difficulty!="hard":
        print("That is not a valid response.")



if difficulty == "easy":
    print("Fill in the gaps")
    easyMode()
elif difficulty == "medium":
    print("Fill in the gaps")
    mediumMode()
else:
    print ("Fill in the gaps")
    hardMode()

print("Thanks for playing!")
    
