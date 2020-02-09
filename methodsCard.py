def reverse(values):
    return values[::-1]


def listOddPositions(values):
    oddValues = [x if i % 2 == 0 else x * 2 for i, x in enumerate(values)]
    # oddValues = [num for num in values if num % 2 != 0]
    print(oddValues)
    return oddValues


def listEvenPositions(values):
    evenValues = values[::2]
    print(evenValues)
    return evenValues


def sumOfDigits(values):
    if values < 10:
        return values
    else:
        sum = (values % 10) + (values // 10)
        return sum
