students = []

def add_student():
    id = input("Enter Student ID: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    student = {"id": id, "name": name, "marks": marks}
    students.append(student)
    print("Student Added Successfully!")

def view_students():
    if not students:
        print("No records found.")
    else:
        for s in students:
            print(s)

def search_student():
    sid = input("Enter ID to search: ")
    for s in students:
        if s["id"] == sid:
            print(s)
            return
    print("Student not found!")

def delete_student():
    sid = input("Enter ID to delete: ")
    for s in students:
        if s["id"] == sid:
            students.remove(s)
            print("Deleted Successfully!")
            return
    print("Student not found!")

while True:
    print("\n1.Add 2.View 3.Search 4.Delete 5.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        break
    else:
        print("Invalid choice")