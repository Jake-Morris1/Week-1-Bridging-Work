# a program to work out the frequency of characters in a string.
# 18-05-2020
# Jake Morris

alphabet=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
alphabetIndex=0

sentence=input("Enter a sentence. ")

while alphabetIndex<26:
    letter=alphabet[alphabetIndex]
    counter=sentence.count(letter)
    if counter != 0:
        print(letter, "is shown", counter, "times.")
    alphabetIndex=alphabetIndex+1
