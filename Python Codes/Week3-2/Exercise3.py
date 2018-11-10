candyList = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish",
             "Skittles", "Hershey Bar", "Skittles", "Starbursts", "M&Ms"]

# The amount of candy the user will be allowed to choose
allowance = 5

# The list used to store all of the candies selected inside of
candyCart = []

for candy in candyList:
    print("[" + str(candyList.index(candy)) + "]" + candy)

for i in range(allowance):
    choice = int(input('Enter 0-9 corresponding to the candy you want to choose: '))
    candyCart.append(candyList[choice])

for candy in candyCart:
    print({candy})