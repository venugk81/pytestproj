# Write a Python program that simulates a simple dictionary for translating English words to Spanish.
# Define a dictionary containing a few English words as keys and their corresponding Spanish translations
# as values. Allow users to enter an English word, and
# then display its Spanish translation if it exists in the dictionary.(use google for English to Spanish translator)

eng_spanish = {
    "hi": "Hola",
    "learning":"aprendiendo",
    "python": "pitón",
    "is":"es",
    "easy": "fácil"
}

##add user:
word = input("enter english word to check its spanish translation: ")
if word in eng_spanish.keys():
    print(eng_spanish[word])
else:
    print("Not found. Try any of these words: ", eng_spanish.keys())
