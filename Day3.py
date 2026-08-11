# Mini Project 
# Variables & List
students=[]

# Dictionaries
student1={"name": "Ashwathy","age": 22, "course":"MSc Computer Science"}
students.append(student1)

# Functions
def add_student(name, age, course):
    student = {"name": name, "age": age, "course": course}
    students.append(student)

def display_students():
    for s in students:
        print(f"{s['name']} - {s['age']} years - {s['course']}")

# Loops
for i in range(3):
    name=input("Enter name:")
    age= int(input("Enter the age:"))
    course= input("Enter the Course:")
    add_student(name,age,course)
    
# File Handling
# Save to file
with open("students.txt", "w") as f:
    for s in students:
        f.write(f"{s['name']},{s['age']},{s['course']}\n")

# Read from file
with open("students.txt", "r") as f:
    data = f.readlines()
    print("Saved Records:")
    for line in data:
        print(line.strip())
