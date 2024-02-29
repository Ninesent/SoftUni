text = input()

final_message = ""

last_added_character = ""

for character in text:
    if character != last_added_character:
        final_message += character
        last_added_character = character

print(final_message)
