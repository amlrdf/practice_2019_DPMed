def fibonacci(n):
    # print(n)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(6))

# print(1, 2, sep='-', end='****')
# print(3, 4)