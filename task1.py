
students = {
    "Alice": 85,
    "Sneha": 92,
    "Rohan": 78,
    "Priya": 88,
    "Karan": 95
}


name = input("Enter the student's name: ")


if name in students:
    print(f"{name}'s marks : {students[name]}")
else:
    print("Student not found.")
