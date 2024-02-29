import re

sentence = input()
search_word = input()

pattern = fr"(?i)\b{search_word}\b"
matches = re.findall(pattern, sentence)

print(len(matches))