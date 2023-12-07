class Card:
    def __init__(self, id, winning_numbers, my_numbers, instances=1) -> None:
        self.id = id
        self.winning_numbers = set(winning_numbers)
        self.my_numbers = set(my_numbers)
        self.instances = instances

    def won_cards(self):
        return len(self.my_numbers.intersection(self.winning_numbers))

def read_cards(file_path):
    with open(file_path, "r") as file:
        return file.readlines()

def process_cards(card_lines):
    card_list = []
    for card_line in card_lines:
        card_values = card_line.split(": ")[1]
        card = Card(
            int(card_line.split(": ")[0].split(" ")[1]),
            card_values.split("|")[0].replace("  ", " ").split(" "),
            card_values.split("|")[1].replace("  ", " ").split(" "),
        )
        card_list.append(card)
    return card_list

def main():
    card_lines = read_cards("4/input_4.1.txt")
    card_list = process_cards(card_lines)

    total_cards = 0
    for card in card_list:
        for _ in range(card.instances):
            number_of_cards_won = card.won_cards()
            print(f"Card {card.id} has won {number_of_cards_won} cards")

            if number_of_cards_won >= 1:
                for i in range(1, min(number_of_cards_won + 1, len(card_list) - card.id)):
                    card_list[card.id + i].instances += 1

        total_cards += card.instances
    print(f"Sum: {total_cards}")

if __name__ == "__main__":
    main()