# factorial function

# 5 * 4 * 3 * 2 * 1

def factx(x) -> int:
    if x == 1:
        return x
    return x * factx(x - 1)

print(factx(3))



