import random

my_dictionary = {}

with open("slowa_fr_eng.txt","r", encoding="utf-8") as file:
    for line in file:
        words = line.split(";")
        my_dictionary[words[0]] = words[3]



word = random.choice(list(my_dictionary))
translated_word = my_dictionary[word]
print(word," : ",translated_word)