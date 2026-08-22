# Python Lists

# 1. Creating a List
subjects = ["Python", "AI", "ML", "Data Structures"]

print("Subjects:", subjects)


# 2. Accessing List Elements
print("First subject:", subjects[0])
print("Last subject:", subjects[-1])


# 3. Changing List Elements
subjects[1] = "Artificial Intelligence"

print("Updated list:", subjects)


# 4. Adding Elements

# append() - adds one item at the end
subjects.append("Generative AI")
print("After append:", subjects)

# insert() - adds item at a specific position
subjects.insert(1, "C Programming")
print("After insert:", subjects)


# 5. Removing Elements

subjects.remove("ML")
print("After remove:", subjects)

# pop() - removes an item using index
subjects.pop(0)
print("After pop:", subjects)


# 6. List Length
print("Number of subjects:", len(subjects))


# 7. Loop Through a List
print("\nSubjects:")
for subject in subjects:
    print(subject)


# 8. Check if Item Exists
if "Python" in subjects:
    print("Python is in the list.")


# 9. Sorting a List
numbers = [5, 2, 8, 1, 10]

numbers.sort()
print("Sorted numbers:", numbers)


# 10. Reverse a List
numbers.reverse()
print("Reversed numbers:", numbers)
