name = 'arthur tomás '

print(len(name))
print(name.find('u'))
print(name.capitalize())
print(name.lower())
print(name.upper())
print(name.title())
print(name.isdigit())
print(name.isalpha())  # Method returns True if all the characters are letters(Here is False because there's a space)
print(name.count('t'))  # Method returns the number of times the value appears
print(name.replace('t', 's'))
print(f'{name.title()*3}')
