import csv


pos_files = ["french-word-list-adjectives.csv","french-word-list-verbs.csv","french-word-list-nouns.csv"]


# def get_most_popular_words():

def get_most_popular_words(files_list):
    word_list = []

    for file in files_list:
        with open(file,"r") as csv_file:
                    csv_reader = csv.DictReader(csv_file)
                    line_count = 1
                    for row in csv_reader:
                        if line_count >= 3 and line_count < 203:
                            line = str(row[";language:;French;;;;;;;;;;;;;;;;;;;;;;;"])
                            line = line.split(";")
                            word = line[1]
                            word_list.append(word)

                        line_count += 1
    for word in word_list:
        with open("600_french_words.txt","a") as file:
            file.write(word + "\n")

get_most_popular_words(pos_files)