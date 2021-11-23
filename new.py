total = 0


def factorial(num):
    current = num
    total = 1

    if current == 0 or current == 1:
        return 0

    while current > 1:
        total *= current
        current -= 1

    return total


print(factorial(6))
