# Python Strings

# 1. Creating a String
name = "Jayshri"
course = "Artificial Intelligence and Machine Learning"

print("Name:", name)
print("Course:", course)


# 2. Accessing Characters
print("First character:", name[0])
print("Last character:", name[-1])


# 3. String Length
print("Length:", len(name))


# 4. String Slicing
text = "Python"

print("First three characters:", text[0:3])
print("Last three characters:", text[3:])
print("Reverse:", text[::-1])


# 5. String Concatenation
first_name = "Jayshri"
last_name = "Borase"

full_name = first_name + " " + last_name

print("Full Name:", full_name)


# 6. String Methods
message = "  Welcome to Python Programming  "

print("Uppercase:", message.upper())
print("Lowercase:", message.lower())
print("Title:", message.title())
print("Stripped:", message.strip())


# 7. Replace
text = "I am learning Java"

text = text.replace("Java", "Python")

print("Updated text:", text)


# 8. Find
sentence = "Python is useful for AI and ML"

print("Position of AI:", sentence.find("AI"))


# 9. Count
word = "banana"

print("Count of 'a':", word.count("a"))


# 10. Check String
email = "jayshri@example.com"

if "@" in email:
    print("Valid email format")


# 11. f-string
age = 18

print(f"My name is {name} and I am {age} years old.")


# 12. Split
skills = "Python,AI,ML,SQL"

skill_list = skills.split(",")

print("Skills:", skill_list)


# 13. Join
joined_skills = " | ".join(skill_list)

print("Joined Skills:", joined_skills)
