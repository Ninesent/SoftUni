even_string = [word for word in input().split() if len(word) % 2 == 0]

print(*even_string, sep="\n")