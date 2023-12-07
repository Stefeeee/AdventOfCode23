import re
with open("4\input_4.1.txt", "r") as cards:
	cards = cards.readlines()
 
class Card:
    id = ""
    winning_numbers = 0
    my_numbers = 0
    instances = 0
    
    def __init__(self, id, winning_numbers, my_numbers, instances) -> None:
        self.id = id
        self.winning_numbers = winning_numbers
        self.my_numbers = my_numbers
        self.instances = instances

    def won_cards(self):
        cardsWon = 0
        for number in self.my_numbers:
            number = number.strip()
            for winning_number in self.winning_numbers:
                winning_number = winning_number.strip()
                if number == winning_number and number != "" and winning_number != "":
                    # print("number: " + str(number) + " winning: " + str(winning_number))
                    cardsWon += 1
                    
        return cardsWon

cardList = []
for card in cards:
    cardValues = card.split(": ")[1]
    card = Card(int(re.findall('\d+', card.split(": ")[0][::-1])[0][::-1]), cardValues.split("|")[0].replace("  ", " ").split(" "), cardValues.split("|")[1].replace("  ", " ").split(" "), 1)
    print(card.id)
    cardList.append(card)

totalCards = 0
for card in cardList:
    numberOfCardsWon = card.won_cards()
    print("Card "+str(card.id) + " has won " + str(numberOfCardsWon)+ " cards ("+ str(card.instances)+ " instances)")
    i = 0
    while i < card.instances:
        
        if numberOfCardsWon >= 1:
            # get next card (bsp currewnt id = 1 index next also 1)
            cardList[card.id].instances += 1
        if numberOfCardsWon >= 2:
            cardList[card.id+1].instances += 1
        if numberOfCardsWon >= 3:
            cardList[card.id+2].instances += 1
        if numberOfCardsWon >= 4:
            cardList[card.id+3].instances += 1
        if numberOfCardsWon >= 5:
            cardList[card.id+4].instances += 1
        if numberOfCardsWon >= 6:
            cardList[card.id+5].instances += 1
        if numberOfCardsWon >= 7:
            cardList[card.id+6].instances += 1
        if numberOfCardsWon >= 8:
            cardList[card.id+7].instances += 1
        if numberOfCardsWon >= 9:
            cardList[card.id+8].instances += 1
        if numberOfCardsWon >= 10:
            cardList[card.id+9].instances += 1
        if numberOfCardsWon >= 11:
            cardList[card.id+10].instances += 1
        i += 1
        
    totalCards += card.instances
print("Sum: "+ str(totalCards))
    
	

        
            
