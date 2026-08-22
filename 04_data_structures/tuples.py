# Python Tuples

# 1. Creating a Tuple
subjects = ("Python", "AI", "ML", "Data Structures")

print("Subjects:", subjects)


# 2. Accessing Tuple Elements
print("First subject:", subjects[0])
print("Last subject:", subjects[-1])


# 3. Tuple Length
print("Number of subjects:", len(subjects))


# 4. Loop Through a Tuple
print("\nSubjects:")
for subject in subjects:
    print(subject)


# 5. Check if Item Exists
if "Python" in subjects:
    print("Python is present.")


# 6. Tuple with Different Data Types
student = ("Jayshri", 18, "AI/ML", True)

print("\nStudent Information:")
print(student)


# 7. Tuple Unpacking
name, age, course, is_student = student

print("Name:", name)
print("Age:", age)
print("Course:", course)
print("Student:", is_student)


# 8. Count
numbers = (10, 20, 10, 30, 10)

print("Count of 10:", numbers.count(10))


# 9. Index
print("Index of 30:", numbers.index(30))
