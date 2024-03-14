student_list = []
student_dict = {}

name = input("Enter your name:")
age = input("Enter your age:")
grade = input("Enter your grade:")

student_list.append(name)
student_dict[name] = {"age": age, "grade": grade}
print("Student information added successfully!")
print(student_dict.items())

search_name = input("Enter the name of the  student to search or simply enter to skip:")
if search_name in student_list:
    info = student_dict[search_name]
    print(f"Name: {search_name}, Age: {info['age']}< Grade: {info['grade']}")
else:
    print("Student not found!")

remove_name = input("Enter the name of the student to remove or simply enter to skip: ")
if remove_name in student_list:
    del student_dict[remove_name]
    student_list.remove(remove_name)
    print("Student removed successfully!")
else:
    print("Student not found!")
    

