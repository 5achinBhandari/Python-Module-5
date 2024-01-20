import random


num_dice = int(input("Enter the number of dice to roll: "))


total_sum = 0


for _ in range(num_dice):

    die_roll = random.randint(1, 6)


    print(f"Dice {_ + 1}: {die_roll}")


    total_sum += die_roll


print(f"Sum of {num_dice} dice rolls: {total_sum}")
