import string
import random

def password_generator(length):
    if length < 1:
        return "Error! Password length must be at least 1."

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return

    password = password_generator(length)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
