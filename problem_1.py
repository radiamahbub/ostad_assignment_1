'''
Problem 1: Student Grade Calculator
Write a Python program that:
1. Takes a student's name as input.
2. Takes marks for 3 subjects.
3. Calculates:
o Total marks
o Average marks
4. Determines the grade using:
o 80–100 → A+
o 70–79 → A
o 60–69 → B
o 50–59 → C
o Below 50 → F
5. Displays the result using a formatted string (f-string).
Example Output
Student Name: Rahim
Total Marks: 245
Average: 81.67
Grade: A+

'''
all_student = []


def add_student():
    s_name = input("Enter Student Name: ")

    math = int(input("Enter The Marks for Mathematics:"))
    bangla = int(input("Enter The Marks for Bangla: "))
    english = int(input("Enter The Marks for English: "))

    total_marks = math + bangla + english
    ave_marks = (math + bangla + english)/3

    s_grade = grade(ave_marks)

    s_data = {
        "s_name": s_name,
        "math": math,
        "bangla": bangla,
        "english": english,
        "total_marks": total_marks,
        "ave_marks": ave_marks,
        "grade": s_grade
    }

    all_student.append(s_data)
    print('Student Addedd Successfully!')


def view_student():
    for student in all_student:
        print(f"Student Name: {student['s_name']}")
        print(f"Math: {student['math']}")
        print(f"Bangla: {student['bangla']}")
        print(f"English: {student['english']}")
        print(f"Total Marks: {student['total_marks']}")
        print(f"Average: {student['ave_marks']:.2f}")
        print(f"Grade: {student['grade']}")


def grade(ave_marks):
    if 80 <= ave_marks <= 100:
        return "A+"
    elif 70 <= ave_marks < 80:
        return "A"
    elif 60 <= ave_marks < 70:
        return "B"
    elif 50 <= ave_marks < 60:
        return "C"
    elif 0 <= ave_marks < 50:
        return "F"
    else:
        return "No Grade Found!"                


while True:
    print("Student Grade Calculator")
    print("""
    1. Add Student
    2. View Students
    3. Exit
    """)

    select = int(input("Select from here: "))

    if select == 1:
        add_student()
    elif select == 2:
        view_student()
    elif select == 3:
        print("Done!")
        break
    else:
        print("Enter Valid Input (1 to 3)")