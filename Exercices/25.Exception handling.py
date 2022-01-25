try:
    numerator = int(input("Enter a numerator: "))
    denominator = int(input("Enter a denominator: "))
    result = numerator/denominator
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero, dummy!")
except ValueError as e:
    print(e)
    print("You didn't enter a number, pay attention!")
except Exception as e:
    print(e)
    print("Something went wrong :(")
else:
    print(result)
finally:
    print("This will always execute!")

