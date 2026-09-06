# Python File Handling

# 1. Write to a File
with open("student.txt", "w") as file:
    file.write("Name: Jayshri Borase\n")
    file.write("Course: B.Tech AI/ML\n")
    file.write("University: DBATU University\n")

print("Data written successfully.")


# 2. Read from a File
with open("student.txt", "r") as file:
    data = file.read()

print("\nStudent Information:")
print(data)


# 3. Append Data to a File
with open("student.txt", "a") as file:
    file.write("Year: 2nd Year\n")

print("Data appended successfully.")


# 4. Read File Line by Line
with open("student.txt", "r") as file:
    print("\nReading line by line:")

    for line in file:
        print(line.strip())


# 5. Check if File Exists
import os

if os.path.exists("student.txt"):
    print("\nFile exists.")
else:
    print("\nFile does not exist.")


# 6. File Modes
# "r" = Read
# "w" = Write
# "a" = Append
# "x" = Create
