def hello(**kwargs):
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")


hello(title="Sr.", first="Arthur", middle="Cohen", last="Barzilay")
