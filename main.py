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
score = 0
for q in range(RandomQ):
    x = random.randint(lowestN,highestN)
    y = random.randint(1,10)
    if Operation == 1:
        print(f"{x}+{y} =?")
        ans = x+y
    if Operation == 2:
        print(f"{x}-{y} =?")
        ans = x-y
    if Operation == 3:
        print (f"{x}*{y} =?")
        ans = x*y
    if Operation == 4:
        x = x*y
        print(f"{x}/{y} =?")
        ans = x//y
    # Read in answer from user
    useranswer= int(input())
    if ans == useranswer:
        print("Correct")
        score +=1
    else:
        print("Nope. You should have said",ans)
print(f"You got {score} questions right out of {RandomQ}!")
