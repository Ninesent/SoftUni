jury_numbers = int(input())
presentation_name = input()


jury_score_count = 0
average_sum = 0
avg_score = 0
total_score = 0



while presentation_name != "Finish":
    avg_score = 0
    for i in range(jury_numbers):
        jury_score_count += 1
        score = float(input())
        total_score += score
        avg_score += score
    avg_score /= jury_numbers
    print(f"{presentation_name} - {avg_score:.2f}.")


    presentation_name = input()

total_score /= jury_score_count

if presentation_name == "Finish":
    print(f"Student's final assessment is {total_score:.2f}.")

