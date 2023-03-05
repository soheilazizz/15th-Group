counter = 0
sump = 0
while True:
    number = input("please enter an integer number")
    if number.lower() == 'q' or number.lower() == 'quit':
        break
    if not number.isdigit():
        continue
    else:
        counter = counter + 1
        sump = sump + int(number)
print(f'the average = {sump / counter}')
    # lowercase of string E: aBC=abc
# isdigit: Check if all the characters in the text are digits



