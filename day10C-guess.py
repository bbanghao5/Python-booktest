import random

n = random.randint(1, 30)

while True:
    x = input("What is your guess? ")
    g = int(x)

    if g == n:
        print("Correct!")
        break
    elif g < n:
        print("Too small")
    else:
        print("Too big")

