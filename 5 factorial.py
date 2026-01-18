n=int(input("Enter a number:"))
if n < 0:
    print("Factorial not defined for negative numbers")

factorial = 1
for i in range(1, n + 1):
    factorial *= i     

print(f'Factorial of {n} is : {factorial}')