with open("slowa_fr_eng.txt","r",encoding="utf-8") as file:
    dictionary = {}
    for line in file:
            line = line.split(";")
            dictionary[str(line[0])] = str(line[3])



