
from time   import sleep
from random import randint

def line (size=80):
    for c in range(0, size):
        print("=", end='')
    print("")


line()
text1 = "| Hello, I'm your computer and I thought a number between 1 and 100!           |"
for t in text1:
    print(t, end='')
    sleep(0.03)
print()

computer = randint (0, 100)

while True:
    print("| " + ("-" * 76) + " |")
    user = int(input("  Try to guess: "))

    if(0 < user <= 100):

        if (user == computer):
            print("| You won!", end='')
            print(" " * 69 + "|")
            line()
            break
        elif (user > computer):
            print("| Lower", end='')
            print(" " * 72 + "|")
        else:
            print("| Higher", end='')
            print(" " * 71 + "|")

    else:
        print("| Invalid number!", end='')
        print(" " * 62 + "|")

v1 = "|     \\"
v2 = "|     (o)>"
v3 = "|    /   /\\"
v4 = "|     - -"

for text in v1:
    print(text, end='')
    sleep(0.1)
print()
for text in v2:
    print(text, end='')
    sleep(0.1)
print()
for text in v3:
    print(text, end='')
    sleep(0.1)
print()
for text in v4:
    print(text, end='')
    sleep(0.1)
print()

vetor = "| Thanks for using GalloGame!"

for letter in vetor:
    print(letter, end='')
    sleep(0.03)
print()

line()