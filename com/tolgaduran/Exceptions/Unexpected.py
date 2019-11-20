myArray = [1, 2, 3]
print(myArray[2])
# print(myArray[3])         => Gives "IndexError" exception

myDict = {'a': 1}
print(myDict['a'])
# print(myDict['b'])        => Gives "KeyError" exception

# for item in [1, 2, 3, 4, 5]:
#     print(myArray[item])  => Gives "IndexError" exception
#     print(item)

for item in [1, 2, 3, 4, 5]:
    try:
        print(myArray[item])
    except IndexError:
        print("The element is not in the list!!!")
