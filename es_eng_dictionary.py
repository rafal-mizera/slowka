with open("slowa_es_eng.txt","r",encoding="utf-8") as file:
    dictionary = {}
    for line in file:
            line = line.split("\t")
            dictionary[str(line[1])] = str(line[2].strip("\n"))


