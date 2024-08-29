# take three positional arguments and return them as a tuple

def argument_t0_tuple(num1, num2, num3):
    return (num1, num2, num3)

num1 = int(input("Enter any number: "))
num2 = int(input("Enter any number: "))
num3 = int(input("Enter any number: "))

print(argument_t0_tuple(num1, num2, num3))
