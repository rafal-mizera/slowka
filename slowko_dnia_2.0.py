"""aplikacja pobierająca losowe słowa w języku francuskim i hiszpańskim wraz z tłumaczeniami oraz zapisująca je w pliku tekstowym """

import random
import tkinter
import fr_eng_dictionary
import es_eng_dictionary
import words_to_file_saver


# losuje z bazy i zwraca parę francuskich słów
def random_fr_word_draw():
    with open("600_french_words.txt","r") as file:
        word_list = []
        for line in file:
            word_list.append(line.strip("\n"))
        word = random.choice(word_list)

        try:
            translated_word = str(fr_eng_dictionary.dictionary[word])
        except KeyError:
            word = random_fr_word_draw()
            translated_word = str(fr_eng_dictionary.dictionary[word])

        fr_words_pair = f'fr. "{word}"- eng. "{translated_word}"'
    return fr_words_pair


# losuje z bazy i zwraca parę hiszpanskich słów
def random_es_word_draw():
    words_pair_list = []
    for key,value in es_eng_dictionary.dictionary.items():
        words_pair = f'es. "{key}"- eng. "{value}"'
        words_pair_list.append(words_pair)
    return random.choice(words_pair_list)


# wyświetla w nowym oknie wylosowane pary słów
def show_word_of_the_day():
    extra_window = tkinter.Toplevel(root)
    extra_window.geometry("500x350")
    welcome = tkinter.Label(master=extra_window,text="Oto słowa na dziś:",font=("Times New Roman",16),bd=64)
    welcome.pack()
    fr_word_of_the_day = tkinter.Label(master=extra_window,text=random_fr_word_draw(),font=("Times New Roman",20),
                                       anchor="center")
    fr_word_of_the_day.pack()
    es_word_of_the_day = tkinter.Label(master=extra_window,text=random_es_word_draw(),font=("Times New Roman",20),
                                       anchor="center")
    es_word_of_the_day.pack()
    # draw_your_word_button.destroy()
    words_to_file_saver.words_saver(random_fr_word_draw())
    words_to_file_saver.words_saver(random_es_word_draw())

    return


# tworzy nowe okno tkinter wraz z przyciskiem pozwalającym losowac słowa
root = tkinter.Tk()
root.title("Slowko dnia 2.0")
root.iconbitmap(default="Dictionary_30019.ico")
root.geometry("640x380")
draw_your_word_button = tkinter.Button(master=root,text="Wylosuj słowa na dziś",command=show_word_of_the_day)
draw_your_word_button.pack()

root.mainloop()
