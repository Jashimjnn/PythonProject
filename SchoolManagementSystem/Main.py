# from School import School
# from Person import Student, Teacher
# from Subject import Subject
# from Classroom import ClassRoom

# school = School("ABC", "Dhaka")

# # Adding Classroom
# eight = ClassRoom("Eight")
# nine = ClassRoom("Nine")
# ten = ClassRoom("Ten")

# school.add_classroom(eight)
# school.add_classroom(nine)
# school.add_classroom(ten)

# # Adding Student
# rahim = Student("Rahim", eight)
# karim = Student("Karim", nine)
# fahim = Student("Fahim", ten)
# hamim = Student("Hamim", ten)

# school.student_admission(rahim)
# school.student_admission(karim)
# school.student_admission(fahim)
# school.student_admission(hamim)

# # Adding Teachers
# abul = Teacher("Abul Khan")
# babul = Teacher("Babul Khan")
# kabul = Teacher("Kabul Khan")

# # Adding Subjects
# bangla = Subject("Bangla", abul)
# physics = Subject("Physics", babul)
# chemistry = Subject("Chemistry", kabul)
# biology = Subject("Biology", kabul)

# eight.add_subject(bangla)
# eight.add_subject(physics)
# eight.add_subject(chemistry)
# nine.add_subject(biology)
# nine.add_subject(physics)
# nine.add_subject(chemistry)
# ten.add_subject(chemistry)
# ten.add_subject(physics)
# ten.add_subject(bangla)
# ten.add_subject(biology)

# eight.take_semester_final_exam()
# nine.take_semester_final_exam()
# ten.take_semester_final_exam()

# print(school)


# Assuming you have defined the School, Student, Teacher, Subject, and ClassRoom classes in their respective modules

from School import School
from Person import Student, Teacher
from Subject import Subject
from Classroom import ClassRoom

# Initialize the school
school = School("ABC", "Dhaka")

# Create classrooms
eight = ClassRoom("Eight")
nine = ClassRoom("Nine")
ten = ClassRoom("Ten")

# Add classrooms to the school
school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

# Main interactive loop
while True:
    print("\n--- School Management System ---")
    print("1. Admit new student")
    print("2. Add new teacher")
    print("3. Add subject to a class")
    print("4. Take semester exam")
    print("5. View school info")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        # Admit new student
        student_name = input("Enter student name: ")
        class_name = input("Enter class (Eight, Nine, Ten): ")
        if class_name == "Eight":
            new_student = Student(student_name, eight)
            school.student_admission(new_student)
        elif class_name == "Nine":
            new_student = Student(student_name, nine)
            school.student_admission(new_student)
        elif class_name == "Ten":
            new_student = Student(student_name, ten)
            school.student_admission(new_student)
        else:
            print("Invalid class name.")

    elif choice == "2":
        # Add new teacher
        teacher_name = input("Enter teacher name: ")
        new_teacher = Teacher(teacher_name)
        print(f"Teacher {teacher_name} added.")

    elif choice == "3":
        # Add subject to a class
        subject_name = input("Enter subject name: ")
        teacher_name = input("Enter teacher name: ")
        new_teacher = Teacher(teacher_name)  # Assume you add the teacher here
        new_subject = Subject(subject_name, new_teacher)

        class_name = input("Enter class (Eight, Nine, Ten): ")
        if class_name == "Eight":
            eight.add_subject(new_subject)
        elif class_name == "Nine":
            nine.add_subject(new_subject)
        elif class_name == "Ten":
            ten.add_subject(new_subject)
        else:
            print("Invalid class name.")

    elif choice == "4":
        # Take semester exam
        class_name = input("Enter class for exam (Eight, Nine, Ten): ")
        if class_name == "Eight":
            eight.take_semester_final_exam()
        elif class_name == "Nine":
            nine.take_semester_final_exam()
        elif class_name == "Ten":
            ten.take_semester_final_exam()
        else:
            print("Invalid class name.")

    elif choice == "5":
        # View school information
        print(school)

    elif choice == "6":
        # Exit the loop
        print("Exiting the system. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
