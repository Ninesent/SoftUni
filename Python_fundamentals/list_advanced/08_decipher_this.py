words_to_decipher = input().split()
deciphered_list = []

for word in words_to_decipher:
    digits_list = []
    letters_list = []
    for symbol in word:
        if symbol.isdigit():
            digits_list.append(symbol)
        else:
            letters_list.append(symbol)

    letters_list[0], letters_list[-1] = letters_list[-1], letters_list[0]
    deciphered_digits, deciphered_letters = "".join(digits_list), "".join(letters_list)
    first_word = chr(int(deciphered_digits))
    deciphered_word = first_word + deciphered_letters
    deciphered_list.append(deciphered_word)

print(*deciphered_list)
