book_pages = int(input())
pages_per_hour = int(input())
days = int(input())

hours_per_day = (book_pages / pages_per_hour) / days

print(int(hours_per_day))

