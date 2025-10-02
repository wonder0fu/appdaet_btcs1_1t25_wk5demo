# Problem: Create a script where it will continuously add numbers and show the crrent sum until you enter a negative numner.

sum = 0
num = int(input("Enter a number: (negative to quit)"))
while num >= 0:
    sum += num
    print(f"Sum is {sum}")
    num = int(input("Enter a number: (negative to quit)"))

print("Negative number entered. Program will now exit.")