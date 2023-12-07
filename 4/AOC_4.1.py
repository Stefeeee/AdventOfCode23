with open("4\input_4.1.txt", "r") as cards:
	cards = cards.readlines()
 
 
def calculate_points(winning_numbers, my_numbers):
    points = 0
    for number in my_numbers:
        number = number.strip()
        for winning_number in winning_numbers:
            winning_number = winning_number.strip()
            if number == winning_number and number != "" and winning_number != "":
                print("number: " + str(number) + " winning: " + str(winning_number))
                if(points == 0):
                    points += 1
                else:
                    points = points*2
    return points

points_sum = 0
for card in cards:
    cardId = card.split(": ")[0]
    cardValues = card.split(": ")[1]
    winning_numbers = cardValues.split("|")[0].replace("  ", " ").split(" ")
    my_numbers = cardValues.split("|")[1].replace("  ", " ").split(" ")
    points = calculate_points(winning_numbers, my_numbers)
    print(cardId + " has " + str(points)+ " points")
    points_sum += points
    
print("Sum: "+ str(points_sum))
    
	

        
            
