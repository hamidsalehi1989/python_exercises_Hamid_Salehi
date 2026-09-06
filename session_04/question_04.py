total = 0

while True:
    number = int(input("Enter a number (0 to exit): "))

    if number == 0:
        break

    total += number

print("The sum is:", total)
  