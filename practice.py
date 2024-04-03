
name = input("Please enter your  name:")
num1 = float(input("Enter your first number:"))
num2 = float(input("Enter your second name:"))
addition_result = num1 + num2
subtraction_result = num1 - num2
multiplication_result = num1 * num2

if num1 != 0:
    division_result = num1 / num2
else:
    division_result = "Undefined"

print(f"Hello {name}")
print(f"The sum of {num1} and {num2} is: {addition_result}")
print(f"The difference of {num1} and {num2} is: {subtraction_result}")
print(f"The product of {num1} and {num2} is: {multiplication_result}")
print(f"The quotient of {num1} and {num2} is: {division_result}")

