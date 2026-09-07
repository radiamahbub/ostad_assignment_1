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

def student():
    s_name = input("Enter Student Name: ")
    math = input("Enter The Marks for Mathematics:")
    bangla = input("Enter The Marks for Bangla: ")
    english = input("Enter The Marks for English: ")

    s_data = {
        "s_name": s_name,
        "math": math,
        "bangla": bangla,
        "english": english
        
    }

    all_student.append(s_data)


    
    


total_marks = math + bangla + english
average_marks = (math + bangla + english)/3

 

if average_marks >= 80 and <= 100:
    print("A+")
elif average_marks >= 70 and <= 79:
    print("A")  
elif average_marks >= 60 and <= 69:
    print("B") 
elif average_marks >= 50 and <= 59:
    print("C")
elif average_marks <= 50:
    print("F")                 