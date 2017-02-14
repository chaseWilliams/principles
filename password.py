import string

uppercase = list(string.ascii_uppercase)
lowercase = list(string.ascii_lowercase)
numbers = [str(x) for x in range(0, 10)]

weight_counts = {
    'lowercase': 0,
    'uppercase': 0,
    'numbers': 0,
    'symbols': 0
}

def update_weights(password):
    for letter in password:
        # lowercase letters
        if letter in lowercase:
            weight_counts['lowercase'] += 1
        # uppercase letters
        elif letter in uppercase:
            weight_counts['uppercase'] += 1
        # numbers
        elif letter in numbers:
            weight_counts['numbers'] += 1
        # symbols
        else:
            weight_counts['symbols'] += 1

def compute_score(password):
    score = 0
    # initial benefit of password length
    score += len(password) * 4
    ## determine benefits
    # lowercase
    score += (len(password) - weight_counts['lowercase']) * 2
    # uppercase
    score += (len(password) - weight_counts['uppercase']) * 2
    # numbers
    score += weight_counts['numbers'] * 4
    # symbols
    score += weight_counts['symbols'] * 6

    ## determine deficits
    if weight_counts['numbers'] is 0 and weight_counts['symbols'] is 0:
        # if all lowercase
        if weight_counts['lowercase'] is 0:
            score -= weight_counts['lowercase']
        # if all uppercase
        if weight_counts['uppercase'] is 0:
            score -= weight_counts['uppercase']
    # return the computed score
    return score

def check_password(password):
    update_weights(password)
    return compute_score(password)

# start program
print('Welcome to the Password Checker Program!')
user_password = input("What is your password?\n> ")

user_score = check_password(user_password)

print(user_score)
# give feedback
if user_score > 85:
    print('Strong Password')
elif user_score > 55:
    print('Medium Password')
else:
    print('Weak Password')
