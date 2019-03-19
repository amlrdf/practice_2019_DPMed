n = 10
z = [1]*2
for idx in range(2, n):
    next = z[idx-1] + z[idx-2]    # Note: next is not a good variable name since it is a built-in function.
                                  # Using it as a variable will mask the function
    z.append(next)
print(z)