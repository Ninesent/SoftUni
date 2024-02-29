n1 = int(input())
n2 = int(input())
m_operator = input()

result = 0

if m_operator == "+":
    result = n1 + n2
    even_or_odd = ""
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"

    print(f"{n1} {m_operator} {n2} = {result} - {even_or_odd}")

elif m_operator == "-":
    result = n1 - n2
    even_or_odd = ""
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"

    print(f"{n1} {m_operator} {n2} = {result} - {even_or_odd}")
elif m_operator == "*":
    result = n1 * n2
    even_or_odd = ""
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"

    print(f"{n1} {m_operator} {n2} = {result} - {even_or_odd}")
elif m_operator == "/":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        result = n1 / n2
        print(f"{n1} {m_operator} {n2} = {result:.2f}")
elif m_operator == "%":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        result = n1 % n2
        print(f"{n1} {m_operator} {n2} = {result}")
elif m_operator == "-":
    result = n1 + n2
    even_or_odd = ""
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"

    print(f"{n1} {m_operator} {n2} = {result} - {even_or_odd}")