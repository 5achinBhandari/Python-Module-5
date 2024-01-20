'''num = int(input("Enter an integer: "))

if num < 2:
    is_prime = False

else:
    is_prime = True

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break


if is_prime:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
'''

num = int(input("Enter an integer value: "))
if num == 1:
    print(f"{num} is not a prime number.")
elif num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(str(num) + " is not a prime number")
            break
    else:
        print(f"{num} is a prime number.")

else:
    print(f"{num} is not a prime number.")
