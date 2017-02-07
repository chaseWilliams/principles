import string

uppercase = list(string.ascii_uppercase)
lowercase = list(string.ascii_lowercase)
numbers = [str(x) for x in range(0, 10)]

def check_password(password):
    score = 0
    lowercase_count = 0
    uppercase_count = 0
    number_count = 0
    symbol_count = 0
    # initial benefit of password length
    score += len(password) * 4
    for letter in password:

        # lowercase letters
        if letter in lowercase:
            lowercase_count += 1
        # uppercase letters
        elif letter in uppercase:
            uppercase_count += 1
        # numbers
        elif letter in numbers:
            number_count += 1
        # symbols
        else:
            symbol_count += 1

    ## determine benefits
    # lowercase
    score += (len(password) - lowercase_count) * 2
    # uppercase
    score += (len(password) - uppercase_count) * 2
    # numbers
    score += number_count * 4
    # symbols
    score += symbol_count * 6

    ## determine deficits
    if number_count is 0 and symbol_count is 0:
        # if all uppercase
        if lowercase_count is 0:
            score -= uppercase_count
        # if all lowercase
        if uppercase_count is 0:
            score -= lowercase_count

    return score

# start program
print('Welcome to the Password Checker Program!')
user_password = input("give ya password\n> ")

user_score = check_password(user_password)

# give feedback
if user_score > 100:
    print('Strong Password')
elif user_score > 70:
    print('Medium Password')
else:
    print('Weak Password')
