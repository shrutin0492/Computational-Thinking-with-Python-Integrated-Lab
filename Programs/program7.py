# 7.
# Creates a list of student details using dictionaries, including USN, name, DOB, and email. The program then writes this list to a file.

def write_student_details_to_file(student_list, file_path):
    with open(file_path, 'w') as file:
        for student in student_list:
            file.write(f"USN: {student['usn']}\n")
            file.write(f"Name: {student['name']}\n")
            file.write(f"DOB: {student['dob']}\n")
            file.write(f"Email: {student['email']}\n")
            file.write("\n")

def main():
    student_list = []

    n = int(input("Enter the number of students: "))
    for i in range(n):
        print(f"Enter details for student {i + 1}:")
        usn = input("USN: ")
        name = input("Name: ")
        dob = input("DOB: ")
        email = input("Email: ")
        student = {'usn': usn, 'name': name, 'dob': dob, 'email': email}
        student_list.append(student)
        print()

    file_path = 'sample.txt'
    write_student_details_to_file(student_list, file_path)
    print("Student details written to file successfully.")

if __name__ == "__main__":
    main()
