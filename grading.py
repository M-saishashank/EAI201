print("=== Student Grading Tool ===")
print("Add subjects and their scores. Type 'done' to finish.\n")

sum_of_scores = 0
subjects_count = 0

while True:
    subject_name = input("Subject Name (or type 'done' to end): ").strip()
    if subject_name.lower() == "done":
        break

    try:
        score = int(input(f"Marks obtained in {subject_name}: "))
    except ValueError:
        print("Invalid input. Please enter a number.\n")
        continue

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"{subject_name}: {score} marks → Grade: {grade}\n")

    sum_of_scores += score
    subjects_count += 1

if subjects_count > 0:
    avg_score = sum_of_scores / subjects_count

    if avg_score >= 90:
        overall = "A"
    elif avg_score >= 80:
        overall = "B"
    elif avg_score >= 70:
        overall = "C"
    elif avg_score >= 60:
        overall = "D"
    else:
        overall = "F"

    print("==== Overall Performance ====")
    print("Total Marks Scored:", sum_of_scores)
    print("Subjects Entered:", subjects_count)
    print("Average Marks:", round(avg_score, 2))
    print("Final Grade:", overall)

else:
    print("No subjects were entered. Cannot compute grades.")
