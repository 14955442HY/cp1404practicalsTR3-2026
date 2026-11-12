MENU = """1. Show the even numbers from x to y
2. Show the odd numbers from x to y
3. Show the squares of the numbers from x to y
4. Exit the program"""

x = int(input("Enter x: "))
y = int(input("Enter y: "))
print(MENU)
choice = input(">>> ")

while choice != "4":
    if choice == "1":
        number = x
        while number <= y:
            if number % 2 == 0:
                print(number, end=" ")
            number += 1
        print()

    elif choice == "2":
        number = x
        while number <= y:
            if number % 2 != 0:
                print(number, end=" ")
            number += 1
        print()

    elif choice == "3":
        number = x
        while number <= y:
            print(number ** 2, end=" ")
            number += 1
        print()

    else:
        print("Invalid choice")

    print(MENU)
    choice = input(">>> ")

print("Finished.")