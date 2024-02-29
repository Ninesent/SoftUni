symbols = [character for character in input() if character != " "]
letters = {}

for symbol in symbols:
    if symbol not in letters.keys():
        letters[symbol] = 0
    letters[symbol] += 1

for char, occurances in letters.items():
    print(f"{char} -> {occurances}")
