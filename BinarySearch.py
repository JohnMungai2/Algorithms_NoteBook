def Fib(list , target):
    low = 0
    high = len(list) - 1
    while low <= high:
        guess = (low + high) // 2 
        if list[guess] == target:
            return guess
        elif list[guess] < target:
            low = guess + 1
        else:
            high = guess - 1

    return -1

list = [1, 4, 7, 10, 13, 17, 20, 23, 26, 30]

target = 20

print(Fib(list, target))