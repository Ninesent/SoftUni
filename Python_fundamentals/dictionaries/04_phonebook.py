phonebook = {}

while True:
    entry = input()

    if entry.isdigit():
        break

    name, phone_number = entry.split("-")
    phonebook[name] = phone_number

searches = int(entry)

for search in range(searches):
    search_name = input()
    if search_name in phonebook.keys():
        print(f"{search_name} -> {phonebook[search_name]}")
    else:
        print(f"Contact {search_name} does not exist.")