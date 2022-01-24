age = int(input('How old are you? '))

if age > 150:
    print("I think you're a liar!")
elif age >= 100:
    print('You are a legend!')
elif age == 100:
    print('You are a century years old!')
elif age >= 65:
    print('You are an elderly!')
elif age >= 18:
    print("You're an adult!")
elif age >= 0:
    print("You're a child!")
else:
    print("You haven't been born yet!")
