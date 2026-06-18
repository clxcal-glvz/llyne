def get_letter_grade(grade):
    # Logic to convert numerical score to a letter grade
    if grade >= 90:     # Threshold 1
        return "A"
    elif grade >= 80:   # Threshold 2
        return "B"
    elif grade >= 70:   # Threshold 3
        return "C"
    elif grade >= 60:   # Threshold 4
        return "D"
    else:
        return "F"

def check_pass_or_fail(grade):
    # Logic to determine if the student passed or failed
    if grade >= 75:     # Passing Mark
        return "PASSED"
    else:
        return "FAILED"

def save_student_record(first_name, last_name, grade, letter_grade, status):
    # Logic to record the data permanently in 'student_records.txt' using append mode
    with open('student_records.txt', "a") as file:
        file.write(f"Name: {first_name} {last_name} | Grade: {grade} | Letter: {letter_grade} | Status: {status}\n")

# Main Loop
while True:
    print("\n--- ADD STUDENT RECORD ---")
    # INPUT SECTION: Collect names and numerical grade
    first_name = input("Enter student's first name: ")
    last_name = input("Enter student's last name: ")
    numerical_grade = float(input("Enter numerical grade (0-100): "))
    
    # PROCESSING SECTION: Call the logic functions above
    letter = get_letter_grade(numerical_grade)
    status = check_pass_or_fail(numerical_grade)
    
    # OUTPUT SECTION: Print results and commit to file
    print(f"\nResult for {first_name} {last_name}:")
    print(f"Letter Grade: {letter}")
    print(f"Status: {status}")
    
    save_student_record(first_name, last_name, numerical_grade, letter, status)
    print("Record saved successfully.")
    
    choice = input("\ Do you want to add another student? (yes/no): ").lower()
    if choice != "yes":
        # EXIT SECTION
        print("Exiting Grade Management System. Review your 'student_records.txt' file for saved data!")
        break