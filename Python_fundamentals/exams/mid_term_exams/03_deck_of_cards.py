deck_of_cards = input().split(", ")
number_of_commands = int(input())


def adding_cards(card_deck: list, card_name: str):
    if card_name not in card_deck:
        card_deck.append(card_name)
        print("Card successfully added")
    else:
        print("Card is already in the deck")


def removing_cards(card_deck: list, card_name: str):
    if card_name in card_deck:
        card_deck.remove(card_name)
        print("Card successfully removed")
    else:
        print("Card not found")


def removing_card_at_index(card_deck: list, index: int):
    if 0 <= index < len(card_deck):
        card_deck.pop(index)
        print("Card successfully removed")
    else:
        print("Index out of range")


def inserting_cards(card_deck: list, index: int, card_name: str):
    if 0 <= index < len(card_deck):
        if card_name not in card_deck:
            card_deck.insert(index, card_name)
            print("Card successfully added")
        else:
            print("Card is already added")
    else:
        print("Index out of range")


for action in range(number_of_commands):
    command = input().split(", ")

    if command[0] == "Add":
        adding_cards(deck_of_cards, command[1])
    elif command[0] == "Remove":
        removing_cards(deck_of_cards, command[1])
    elif command[0] == "Remove At":
        removing_card_at_index(deck_of_cards, int(command[1]))
    elif command[0] == "Insert":
        inserting_cards(deck_of_cards, int(command[1]), command[2])

print(", ".join(deck_of_cards))
