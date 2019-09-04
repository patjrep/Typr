import random
import json, codecs
import time as t
import datetime as dt
from quotes_list import quote_list
import csv


#Picks a random sentence to type
def normal_sentences():
    random_sentence_pick = quote_list[random.randint(0,len(quote_list)-1)]
    return random_sentence_pick

#Adds Username and Score to CSV File
def add_score(name, wpm):
    #These next lines can be used to loop through and count #of lines read
    ##with open('scoring.csv') as csv_file:
        ##csv_reader = csv.reader(csv_file, delimiter=',')
        ##print(csv_reader)
        #line_count = 0
        #print(f'Processed {line_count} lines.')
    with open('scoring.csv', 'a') as scores:
        score_tracker = csv.writer(scores, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        score_tracker.writerow([name, wpm])

def main_menu():
    print("~~Welcome~~\n To \n ~The Typing Game~")
    menu_choice = input("What would you like to do?\n(P)lay Game\n(R)ules\n(H)igh Score List\n(Q)uit")
    if menu_choice == 'P' or 'p':
        typing_game()
    elif menu_choice == 'R' or 'r':
        pass
        #game_rules()
    elif menu_choice == 'H' or 'h':
        pass
        #high_scores()
    else:
        quit()
#Actual game mechanics
def typing_game():

    game_start = str(input("Start Game? (Y/N): ")).lower()

    if game_start == 'y':
        print("Get ready...")
        t.sleep(1)
        print("Get Set...")
        t.sleep(1)
        print("Go!")
        random_sentence = normal_sentences()
        number_of_words = len(random_sentence.split())
        time_start = dt.datetime.now()
        player_input = input(("Your sentence is: \n" + '"' + random_sentence + '"' '\n'))
        if player_input == random_sentence:
            time_end = dt.datetime.now()
            print("Complete!")
            time = time_end - time_start
            time_seconds = time.total_seconds()
            print("Your total time was", round(time_seconds, 2))
            wpm = (60 / time_seconds) * number_of_words
            print("You have a typing speed of", round(wpm, 2), "WPM")
            #scores = score_list()
            name = input("What is your name?: ")
            add_score(name, wpm)
        else:
            pass
            #compare the two sentences here to see the accuraccy of the player's typing (maybe split by word or character to get exact percentage match)

    else:
        typing_game()

def main():
    main_menu()

if __name__ == "__main__":
    main()