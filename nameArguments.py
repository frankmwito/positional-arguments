# introduce a person using two names

def persons_name(first_name, second_name):
    return f"{first_name} {second_name}"

first_name = input("Enter your forst name: ")
second_name = input("Enter your second name: ")

print(persons_name(first_name, second_name))