from datetime import datetime,date

def words_saver(content):
    with open(f"Words_to_learn_{str(datetime.now().month)}_{str(datetime.now().year)}.txt","a") as file:
        file.write(f"{date.today()} {content}\n")