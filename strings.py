print('welcome to the string gallery!')
print('today we\'ll see various manipulations and statistics about a string')
string = input("go ahead and give us the name of your city\n> ")
print('Your string is {0} characters long'.format(len(string)))
index = int(input('Choose a number between 0 and %i' % (len(string) - 1)))
print('You chose the {0} index, at which there is a "{1}".'.format(index, string[index]))
print('If split up the city name by each occurence of the character "%s", you get' % string[index])
for substring in string.split(string[index]):
    print(substring)
arr = string.split(string[index])
arr.reverse()
print('if you put them back together in reverse order, you get%s' % \
        ''.join(arr))
print('Replace all instances of {0} with "WOW" gets us {1}'.format( string[index],
        string.replace(string[index], 'WOW')))
print('capitalized: {0}. lowercased: {1}. uppercased: {2}. swapcase: {3}'.format(
    string.capitalize(), string.lower(), string.upper(), string.swapcase()
))
start_index = int(input('choose a start index within the range 0 and %i' % (len(string) - 1)))
end_index = int(input('choose a start index within the range 0 and %i' % (len(string) - 1)))
print('we got this: %s ' % string[start_index : end_index])
print('choose a word in the following phrase: ')
phrase = 'the brown dog jumped over the lazy fox'
choice = input(phrase)
print('you chose a word at the index %i' % phrase.find(choice))
num1 = input('Give us a number')
num2 = input('Give us another number')
print('Combining them gets us %s' % (str(num1) + str(num2)))
