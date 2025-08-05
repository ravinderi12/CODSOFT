import random
import string
def generate_password(length):
    if length<6:
        print("  length of 6 in password provide more security .")
        return  ""

    lowercase= string.ascii_lowercase
    uppercase=string.ascii_uppercase
    digits =string.digits
    special_character= string.punctuation

    all_char= lowercase + uppercase + digits + special_character

    password = [ random.choice(lowercase), random.choice(uppercase), random.choice(digits), random.choice(special_character)]

    password +=random.choices(all_char,k=length-4)
    random.shuffle(password)
    return ''.join(password)

print("Welcome to random  Password Generator!")

try:
    user_length = int(input("Enter desired password length you want : "))
    if user_length<=0:
        print("please enter a positive no. ")
    else:
        password = generate_password(user_length)
        if password:
            print(f"\n Random Generated Password: {password}")
except ValueError:
    print("Invalid numbers .")