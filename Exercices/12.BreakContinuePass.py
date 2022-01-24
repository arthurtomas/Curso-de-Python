#  break =         used to terminate the loop entirely
#  continue =      skips to the nex interation of the loop
#  pass =          does nothing, acts as a placeholder

while True:
    name = input("Enter your name: ")
    if name != "":
        break

phone_number = input("Enter your phone number: ")
for i in phone_number:
    if i == "-":
        continue
    print(i, end="")

for i in range(1, 31):
    if i == 13:
        pass
    print(i, end=" ")

