# Python Sets

# 1. Creating a Set
languages = {"Python", "C", "Java", "Python"}

print("Languages:", languages)


# 2. Adding an Element
languages.add("JavaScript")

print("After adding:", languages)


# 3. Adding Multiple Elements
languages.update(["SQL", "R"])

print("After update:", languages)


# 4. Removing an Element
languages.remove("C")

print("After remove:", languages)


# 5. Discard an Element
languages.discard("HTML")

print("After discard:", languages)


# 6. Check if Element Exists
if "Python" in languages:
    print("Python is available.")


# 7. Set Length
print("Number of languages:", len(languages))


# 8. Set Operations

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Union
print("Union:", set_a | set_b)

# Intersection
print("Intersection:", set_a & set_b)

# Difference
print("Difference:", set_a - set_b)

# Symmetric Difference
print("Symmetric Difference:", set_a ^ set_b)


# 9. Loop Through a Set
print("\nLanguages:")

for language in languages:
    print(language)
