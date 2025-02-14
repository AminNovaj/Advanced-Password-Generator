import random
import string

# All possible characters for password generation
characters = string.ascii_letters + string.digits + string.punctuation

# Header banner
print("+===============================================================================+")
print("|  ____                           ____                    ____                  |")
print("| |  _ \    __ _   ___   ___     / ___|   ___   _ __     |  _ \   _ __    ___   |")
print("| | |_) |  / _` | / __| / __|   | |  _   / _ \ | '_ \    | |_) | | '__|  / _ \  |")
print("| |  __/  | (_| | \__ \ \__ \   | |_| | |  __/ | | | |   |  __/  | |    | (_) | |")
print("| |_|      \__,_| |___/ |___/    \____|  \___| |_| |_|   |_|     |_|     \___/  |")
print("|                                                                               |")
print("+===============================================================================+")
print("\nWelcome To Our Lovely Password Generator! Feel Free To Make Your Passwords <3\n")

# Get password length from user
password_length = int(input("Password Length: "))

# Generate the password
final_password = ''.join(random.choice(characters) for _ in range(password_length))

# Output the result
print(f"\nYour Generated Password Is: {final_password}\n")
