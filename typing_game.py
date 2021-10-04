import random
import json
import time as t
import datetime as dt
from quotes_list import quote_list
import csv
from difflib import SequenceMatcher

# Picks a random sentence to type

def normal_sentences():
    random_sentence_pick = quote_list[random.randint(0, len(quote_list)-1)]
    return random_sentence_pick

# Adds Username and Score to CSV File


def add_score(name, wpm):
    with open('scoring.csv', 'a+') as scores:
        score_tracker = csv.writer(scores)  # , delimiter=',')
        score_row = [(name), (wpm)]
        score_tracker.writerow(score_row)

# Takes the scores_list argument and prints it neatly


def high_score_list(scores_list):
    print("\nUSERNAME | WPM\n-------------")
    print('\n'.join(['\t'.join([str(cell) for cell in row])
                     for row in scores_list]), '\n')
    choice = input("Return to main menu? (Y/N): ")
    if choice.lower() == 'y':
        main_menu()
    else:
        high_score_list(scores_list)

# Appends CSV to a list of lists, removes blank lines from the list, converts str to floats, then returns the list


def score_sorter():
    with open('scoring.csv', newline='') as File:
        reader = csv.reader(File, delimiter=',')
        scores_list = []
        for row in reader:
            scores_list.append(row)
        scores_list = [x for x in scores_list if x != []]
        for score in scores_list:
            score[1] = float(score[1])
        return sorter(scores_list)

# Sorts the list by WPM using bubble sort and lambda, then returns


def sorter(scores_list):
    l = len(scores_list)
    for i in range(0, l):
        for j in range(0, l-i-1):
            if (scores_list[j][1] > scores_list[j + 1][1]):
                tempo = scores_list[j]
                scores_list[j] = scores_list[j + 1]
                scores_list[j + 1] = tempo
    scores_list = sorted(scores_list, key=lambda x: x[1], reverse=True)
    return high_score_list(scores_list)

# Rules of the Game


def game_rules():
    print("\nType the sentence as fast as you can! Good Luck!\n")
    choice = input("Return to main menu? (Y/N): ")
    if choice.lower() == 'y':
        main_menu()
    else:
        game_rules()

# Player menu options


def main_menu():
    print("\n\n\n\n\n\n\n\n\n   ~~Welcome~~\n\n       To\n\n      \n ~The Typing Game~\n\n\n\n")
    menu_choice = input(
        "What would you like to do?\n\n\n(P)lay Game\n\n(R)ules\n\n(H)igh Score List\n\n(Q)uit\n > ")
    if menu_choice in ['P', 'p']:
        typing_game()
        print("Game")
    elif menu_choice in ['R', 'r']:
        game_rules()
    elif menu_choice in ['H', 'h']:
        score_sorter()
    elif menu_choice in ['Q', 'q']:
        print("\nCome Back Soon!\n")
        t.sleep(1)
        quit()

# Actual game mechanics


def typing_game():

    game_start = str(input("\nStart Game? (Y/N): ")).lower()

    if game_start == 'y':
        print("\nGet ready...\n")
        t.sleep(1)
        print("Get Set...\n")
        t.sleep(1)
        print("Go!\n")
        t.sleep(0.5)
        random_sentence = normal_sentences()
        number_of_words = len(random_sentence.split())
        time_start = dt.datetime.now()
        player_input = input(
            ("Your sentence is: \n" + '"' + random_sentence + '"' '\n'))
        if player_input == random_sentence:
            time_end = dt.datetime.now()
            print("Complete!\n")
            t.sleep(0.5)
            time = time_end - time_start
            time_seconds = round(time.total_seconds(), 2)
            print("Your total time was", time_seconds, 'seconds!\n')
            wpm = float(round(((60 / time_seconds) * number_of_words), 2))
            print("You have a typing speed of", wpm, "WPM\n")
            accuracy = 100
            print("You have an accuracy of", accuracy, '%\n')
            #scores = score_list()
            name = input("What is your name?: ")
            print("Added to high scores list!")
            t.sleep(1)
            add_score(name, wpm)
            main_menu()
        else:
            player_input_arr = []
            random_sentence_arr = []
            for char in player_input:
                player_input_arr.append(char)
            for i in random_sentence:
                random_sentence_arr.append(i)
            time_end = dt.datetime.now()
            print("Complete!\n")
            t.sleep(0.5)
            time = time_end - time_start
            time_seconds = round(time.total_seconds(), 2)
            print("Your total time was", time_seconds, 'seconds!\n')
            wpm = float(round(((60 / time_seconds) * number_of_words), 2))
            similarity = round(
                ((SequenceMatcher(None, player_input_arr, random_sentence_arr).ratio()) * 100), 2)
            print("You typed the sentence with ", similarity, " % accuracy!")
            print("\nYou have a typing speed of", wpm, "WPM\n")
            print("\nGet 100% accuracy to be added to the high score list!")
            if similarity == 100:
                name = input("What is your name?: ")
                t.sleep(1)
                add_score(name, wpm)

            main_menu()

    else:
        if game_start in ['N', 'n']:
            print("\nReturning to the Main Menu\n")
            t.sleep(1)
            main_menu()
        else:
            print("Returning to the Main Menu")
            main_menu()


def main():
    main_menu()


if __name__ == "__main__":
    main()


#Optimizations