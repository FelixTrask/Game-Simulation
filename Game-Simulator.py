import math
import random
from collections import Counter

suits = ['hearts', 'diamonds', 'clubs', 'spades']
ranks = list(range(1, 14))

full_deck = [(rank, suit) for rank in ranks for suit in suits]

def draw_card(card_number):
    cards = full_deck.copy()
    card_list = []
    for _ in range(card_number):
        random_card = random.choice(cards)
        card_list.append(random_card)
        cards.remove(random_card)
    return card_list

money = 0
times_ran = 10000000
cards_drawn = 5

count_3_of_a_kind = 0
count_3_face_cards = 0
count_3_same_suit = 0
count_3_non_face = 0
count_5_same_color = 0
count_no_win = 0

for _ in range(times_ran):
    money -= 10
    card_list = draw_card(cards_drawn)

    ranks_drawn = [rank for (rank, suit) in card_list]
    suits_drawn = [suit for (rank, suit) in card_list]
    colors_drawn = ['red' if suit in ['hearts', 'diamonds'] else 'black' for suit in suits_drawn]

    rank_counts = list(Counter(ranks_drawn).values())
    suit_counts = list(Counter(suits_drawn).values())
    red_count = colors_drawn.count('red')
    black_count = colors_drawn.count('black')

    is_win = False

    if rank_counts.count(3) >= 1:
        money += 60
        count_3_of_a_kind += 1
        is_win = True

    if sum(1 for rank in ranks_drawn if rank in [11, 12, 13]) == 3:
        money += 20
        count_3_face_cards += 1
        is_win = True

    if 3 in suit_counts and max(suit_counts) == 3:
        money += 15
        count_3_same_suit += 1
        is_win = True

    if sum(1 for rank in ranks_drawn if rank <= 10) == 3:
        money += 10
        count_3_non_face += 1
        is_win = True

    if red_count == 5 or black_count == 5:
        money += 5
        count_5_same_color += 1
        is_win = True

    if not is_win:
        count_no_win += 1

print("Average money loss/gain: " + str(money / times_ran) + "\n")
print("3 of a kind hits:", count_3_of_a_kind)
print("3 of a kind percentage:", str(100 * (count_3_of_a_kind / times_ran)), "\n")
print("3 face cards hits:", count_3_face_cards)
print("3 face card percentage:", str(100 * (count_3_face_cards / times_ran)), "\n")
print("3 same suit hits:", count_3_same_suit)
print("3 same suit hits percentage:", str(100 * (count_3_same_suit / times_ran)), "\n")
print("3 non-face cards hits:", count_3_non_face)
print("3 non-face cards percentage:", str(100 * (count_3_non_face / times_ran)), "\n")
print("5 same color hits:", count_5_same_color)
print("5 same color percentage:", str(100 * (count_5_same_color / times_ran)), "\n")
print("No win hands:", count_no_win)
print("No win percentage:", str(100 * (count_no_win / times_ran)), "\n")