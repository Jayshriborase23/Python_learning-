# Python Dictionaries

# 1. Creating a Dictionary
student = {
    "name": "Jayshri",
    "age": 18,
    "course": "AI/ML",
    "university": "DBATU University"
}

print("Student:", student)


# 2. Accessing Values
print("Name:", student["name"])
print("Course:", student["course"])


# 3. Using get()
print("Age:", student.get("age"))


# 4. Adding a New Key-Value Pair
student["year"] = 2

print("After adding year:", student)


# 5. Updating a Value
student["age"] = 19

print("Updated age:", student["age"])


# 6. Removing an Item
student.pop("year")

print("After removing year:", student)


# 7. Dictionary Keys
print("Keys:", student.keys())


# 8. Dictionary Values
print("Values:", student.values())


# 9. Dictionary Items
print("Items:", student.items())


# 10. Check if Key Exists
if "name" in student:
    print("Name key exists.")


# 11. Loop Through Dictionary
print("\nStudent Information:")

for key, value in student.items():
    print(key, ":", value)


# 12. Nested Dictionary
students = {
    "student1": {
        "name": "Jayshri",
        "course": "AI/ML"
    },
    "student2": {
        "name": "Mayuri",
        "course": "Computer Science"
    }
}

print("\nNested Dictionary:")
print(students["student1"]["name"])
print(students["student2"]["course"])
