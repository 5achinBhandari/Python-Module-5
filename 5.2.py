numbers = []
while True:
    user_input = input("Enter a number (or press Enter to quit): ")


    if user_input == "":
        break

    try:

        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a valid number.")


numbers.sort(reverse=True)


print("The five greatest numbers (in descending order) are:")
for i, num in enumerate(numbers[:5], start=1):
    print(f"{i}: {num}")



'''user_input = input('Enter numbers or quit by pressing Enter: ')
List = []
max_num = user_input
while (user_input != ''):
    List.append(user_input)
    if(user_input>max_num):
        max_num = user_input
    user_input = input('Enter numbers or quit by pressing Enter: ')
print("Sorted order: ")
List.sort(reverse=True)
for x in List[:5]:

    print(x, end=' ')
'''