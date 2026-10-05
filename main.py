import random

RandomQ= int(input("how many Questions would you like?"))

lowestN = int(input("What is the lowest number?"))

highestN = int(input("What is the highest number?"))

print("What operation would you like?")
print("1-Addition")
print("2-Subtraction")
print("3-Multiplication")
print("4-Division")
Operation = int(input(""))
x = random.randint(1,10)
y = random.randint(1,10)
if Operation == 1:
    print(f"{x}+{y} =?")
