import math
import random

suits = ['hearts', 'diamonds', 'clubs', 'spades']
ranks = list(range(1, 14))

full_deck = [(rank, suit) for rank in ranks for suit in suits]

def draw_card(card_number):
    cards = full_deck.copy()
    card_list = []
    for i in range(card_number):
        random_card = random.choice(cards)
        card_list.append(random_card)
        cards.remove(random_card)
    return card_list

money = 0
times_ran = 1000000
cards_drawn = 5

count_3_of_a_kind = 0
count_3_face_cards = 0
count_3_same_suit = 0
count_3_non_face = 0
count_3_same_color = 0
count_no_win = 0

for i in range(times_ran):
    money -= 10
    card_list = draw_card(cards_drawn)
    
    ranks_drawn = [rank for (rank, suit) in card_list]
    suits_drawn = [suit for (rank, suit) in card_list]
    colors_drawn = ['red' if suit in ['hearts', 'diamonds'] else 'black' for suit in suits_drawn]
    
    if any(ranks_drawn.count(rank) == 3 for rank in set(ranks_drawn)):
        money += 60  # 3 of a kind
        count_3_of_a_kind += 1
    elif sum(1 for rank in ranks_drawn if rank in [11, 12, 13]) == 3:
        money += 20  # 3 face cards
        count_3_face_cards += 1
    elif any(suits_drawn.count(suit) == 3 for suit in set(suits_drawn)):
        money += 15  # 3 of the same suit
        count_3_same_suit += 1
    elif sum(1 for rank in ranks_drawn if rank <= 10) == 3:
        money += 10  # 3 non-face cards
        count_3_non_face += 1
    elif colors_drawn.count('red') == 3 or colors_drawn.count('black') == 3:
        money += 5   # 3 of the same color
        count_3_same_color += 1
    else:
        count_no_win += 1
    


print("Average money loss/gain: " + str(money / times_ran) + "\n")
print("3 of a kind hits:", count_3_of_a_kind)
print("3 of a kind percentage:", str(100*(count_3_of_a_kind/times_ran)), "\n")
print("3 face cards hits:", count_3_face_cards)
print("3 face card percentage:", str(100*(count_3_face_cards/times_ran)), "\n")
print("3 same suit hits:", count_3_same_suit)
print("3 same suit hits percentage:", str(100*(count_3_same_suit/times_ran)), "\n")
print("3 non-face cards hits:", count_3_non_face)
print("3 non-face cards percentage:", str(100*(count_3_non_face/times_ran)), "\n")
print("3 same color hits:", count_3_same_color)
print("3 same color percentage:", str(100*(count_3_same_color/times_ran)), "\n")
print("No win hands:", count_no_win)
print("No win percentage:", str(100*(count_no_win/times_ran)), "\n")