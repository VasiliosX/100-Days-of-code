##Black Jack
##Black Jack
import random


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card(list_of_cards):
    chosen=random.choice(list_of_cards)
    return chosen




def calculate_score(drawn_cards):
    score_in = sum(drawn_cards)
    if len(drawn_cards) == 2:
        if score_in == 21:
            return 0
    if 11 in drawn_cards and score_in > 21:
        drawn_cards.remove(11)
        drawn_cards.append(1)

    score = sum(drawn_cards)
    return score





want=input('Do you want to play BlackJack? Type y for yes and n for no:')

while want=='y':

    user_cards = []

    computer_cards = []

    user_cards.append(deal_card(list_of_cards=cards))

    end = False
    cont = True
    while cont==True and end==False:


        user_cards.append(deal_card(list_of_cards=cards))
        computer_cards.append(deal_card(list_of_cards=cards))
        print(f'The user has {user_cards}')
        print(f'The computer"s first card is {computer_cards[0]}')







        user_score=calculate_score(drawn_cards=user_cards)
        computer_score=calculate_score(drawn_cards=computer_cards)

        print(f"The user's score is {user_score}")

        print(f"The computer's score is {computer_score}")

        if computer_score == 0 or user_score > 21:
            end = True
            print('Game ends, you lose')

        elif computer_score>21 or user_score==0:
            end=True
            print('Game ends, you win')




        if end==False:
            play=input('Type y to get another card, type n to pass: ')

            if play=='n':
                if computer_score>=user_score:
                    print('You lose, computer wins')
                    cont=False
                elif user_score>computer_score:
                    print('You win, the computer loses')
                    cont=False
            elif play=='y':
                cont=True

    want = input('Do you want to play BlackJack? Type y for yes and n for no:')