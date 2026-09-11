import random

print("===== Random Module =====")

# Generate random integer
number = random.randint(1, 100)
print("Random Number:", number)

# Generate random number between 0 and 1
decimal = random.random()
print("Random Decimal:", decimal)

# Choose a random item from a list
fruits = ["Apple", "Mango", "Banana", "Orange"]
fruit = random.choice(fruits)
print("Random Fruit:", fruit)

# Shuffle a list
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print("Shuffled List:", numbers)
