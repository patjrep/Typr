import random
import time as t
import datetime as dt
from quotes_list import quote_list
from scoring import scores


#Picks a random sentence to type
def normal_sentences():
    random_sentence_pick = quote_list[random.randint(0,len(quote_list)-1)]
    return random_sentence_pick

def score_calculator():
    pass

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

    else:
        typing_game()


def main():
    typing_game()

if __name__ == "__main__":
    main()