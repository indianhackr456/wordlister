import random

# Stylish banner
banner = '''
__     ___               _
\ \   / (_)_ __ ___  ___| |__
 \ \ / /| | '__/ _ \/ __| '_ \
  \ V / | | | |  __/\__ \ | | |
   \_/  |_|_|  \___||___/_| |_| [Team Indian Hacker]

'''

# Function to generate possible passwords
def generate_passwords(name, dob, username, keywords, length, num_passwords):
    passwords = set()
    
    for _ in range(num_passwords):
        password = ""

        # Randomly select a keyword followed by a random number
        keyword = random.choice(keywords)
        number = str(random.randint(10**(length-1), (10**length)-1))

        # Combine the selected elements to form a password
        password += keyword.capitalize() if random.choice([True, False]) else keyword.lower()
        password += number

        passwords.add(password)

    return passwords

# Main function
def main():
    print(banner)
    print("Welcome to the Password Generator Tool!")
    print("--------------------------------------\n")

    # Questions to ask the user
    name = input("What is the target's name? ")
    dob = input("When is the target's date of birth? ")
    username = input("What is the target's username? ")
    keywords = input("Enter common keywords related to the target (separated by commas): ").split(",")
    length = int(input("Enter the desired length of the numeric part of the passwords: "))
    num_passwords = int(input("Enter the number of passwords to generate: "))

    # Generate passwords
    passwords = generate_passwords(name, dob, username, keywords, length, num_passwords)

    # Show the generated passwords
    print("\nGenerated Passwords:")
    for password in passwords:
        print(password)

if __name__ == "__main__":
    main()