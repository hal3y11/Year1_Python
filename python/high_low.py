import random

    
card_number = random.randint(1, 13)
    
   
if card_number == 1:
        card_value = "Ace"
elif 2 <= card_number <= 10:
        card_value = str(card_number)
elif card_number == 11:
        card_value = "Jack"
elif card_number == 12:
        card_value = "Queen"
else:
        card_value = "King"
    
    
print("Random Number Generated:" +(str(card_number)))
print("Card Value: "+(str(card_value)))

