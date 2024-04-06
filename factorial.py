# Example: Calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

#num = 6
#print(f"Factorial of {num} is {factorial(num)}")

while True:
    num = input("Enter a number to calculate its factorial. (q to quit) ")
    if num == "q":
        break
    if num.isdigit():
        num = int(num)
        print(f"Factorial of {num}: {factorial(num)}")
    else:
       print(f"Please enter a number, {num} is not a number.")
