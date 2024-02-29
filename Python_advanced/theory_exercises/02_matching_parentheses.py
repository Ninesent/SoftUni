expression = input()
parenthesis_indexes = []

for index in range(len(expression)):
    if expression[index] == "(":
        parenthesis_indexes.append(index)
    elif expression[index] == ")":
        start_index = parenthesis_indexes.pop()
        end_index = index + 1
        print(expression[start_index:end_index])
