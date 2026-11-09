
# Password Generator

import random
import string

print("========== PASSWORD GENERATOR ==========")

while True:

    # Get password length from user
    length = int(input("\nEnter the desired password length: "))

    if length <= 0:
        print("Please enter a valid password length!")
        continue

    # Ask for password complexity
    print("\nSelect password complexity:")
    print("1. Letters only")
    print("2. Letters and Numbers")
    print("3. Letters, Numbers and Special Characters")

    choice = input("\nEnter your choice (1-3): ")

    # Select character combinations
    if choice == "1":
        characters = string.ascii_letters

    elif choice == "2":
        characters = string.ascii_letters + string.digits

    elif choice == "3":
        characters = (
            string.ascii_letters +
            string.digits +
            string.punctuation
        )

    else:
        print("Invalid choice! Please select between 1 and 3.")
        continue

    # Generate password
    password = ''.join(
        random.choice(characters)
        for i in range(length)
    )

    # Display password
    print("\nYour Generated Password is:", password)

    # Ask to generate another password
    again = input("\nGenerate another password? (yes/no): ")

    if again.lower() != "yes":
        print("\nThank you for using Password Generator!")
        break
