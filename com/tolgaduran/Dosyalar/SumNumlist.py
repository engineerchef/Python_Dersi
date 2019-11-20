numFile = open("numbers.list", "r")
nums = numFile.read().splitlines()

sum = 0
for number in nums:
    print(number)
    sum += int(number)

print("\nThe sum of all of your numbers was:")
print(sum)
