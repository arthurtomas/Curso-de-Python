name = "Barzilay"  # Global scope(available inside and outside functions)


def display_name():
    name = "Arthur"  # Local scope(available only inside this function)
    print(name)


display_name()
print(name)
