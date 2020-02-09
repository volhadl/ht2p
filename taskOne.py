from methodsCard import *

print("Enter card number: ")
cardNumber = input()
cardNumber = reverse(cardNumber)
cardNumberList = list(map(int, cardNumber))
print(cardNumberList)
oddList = listOddPositions(cardNumberList)
newList = [sumOfDigits(n) for n in oddList]
print(newList)
sumList = sum(newList)
print(sumList)

if sumList % 10 == 0:
    print("valid")
else:
    print('not valid')
