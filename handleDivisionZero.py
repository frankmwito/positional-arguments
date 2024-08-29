# return the result of dividing two numbers and also handle division by zero

def division(num1, num2):
    if num1 or num2 == 0:
        return "Error: Division by zero is not allowed"
    else:
        result = num1 / num2
        return result
    
num1 = float(input("Enter any number: "))
num2 = float(input("Enter any number: "))

answer = division(num1, num2)

print("The answer for division is", answer)
