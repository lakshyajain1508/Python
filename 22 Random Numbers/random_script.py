# This script generates a specified number of random integers between 1 and 100.
import random

while True:
    try:
        num = int(input("How many random numbers (1-100) would you like to generate? "))
        if num > 100:
            print("Invalid input. You can only generate up to 100 unique numbers in this range.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a whole number.")

# Generate a list of unique random numbers in the specified range.
number = random.sample(range(1, 101), num)

# Sort the generated numbers in ascending order.
number.sort()

print(f"\nGenerating {num} random numbers between 1 and 100:")
for i,number in enumerate(number):
    print(f"{i+1} - {number}")
