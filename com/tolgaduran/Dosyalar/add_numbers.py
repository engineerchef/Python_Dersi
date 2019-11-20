def add(num1, num2):
    return int(num1) + int(num2)


def subtract(num1, num2):
    return int(num1) - int(num2)


def multiply(num1, num2):
    return int(num1) * int(num2)


def divide(num1, num2):
    return int(num1) / int(num2)


num1 = input("Enter 1st Number : ")
num2 = input("Enter 2nd Number : ")
result_list = open('result_list', 'r').read().splitlines()
operator = input("Select an operation to perform => [add, subtract, multiply, divide] : ")

try:
    num1 = int(num1)
    num2 = int(num2)
except TypeError:
    print("Entered Invalid Value!!")
    exit()

if operator == "add":
    result = add(num1, num2)
elif operator == "subtract":
    result = subtract(num1, num2)
elif operator == "multiply":
    result = multiply(num1, num2)
elif operator == "divide":
    result = divide(num1, num2)
else:
    result = 0
    print("Invalid Operator Entered!!!")

result_list.append(result)
print(result_list)

result_file = open('result_list', 'w')

for result in result_list:
    result_file.write(str(result) + "\n")
result_file.close()

print("Your result is : " + str(result))
