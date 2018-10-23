# ase_lab

def sum(m, n):
    result = m
    if n < 0:
        for i in range(abs(n)):
            result -= 1
    else:
        for i in range(n):
            result += 1
    return result

def divide(m, n):
    result = 0
    sign = 1
    if n == 0:
        raise ZeroDivisionError("You cannot divide by 0!")
    if (n < 0 and m > 0) or (n > 0 and m <0):
        sign = -1
    n = abs(n)
    m = abs(m)
    while m-n >= 0:
        m -= n
        result += 1
    return sign * result

def subtract(m, n):
    result = m
    if n < 0:
        for i in range(abs(n)):
            result += 1
    else:
        for i in range(abs(n)):
            result -= 1
    return result

def multiply(m, n):
    sign = 1
    if n == 0 or m == 0:
        return 0
    if (m > 0 and n < 0) or (m < 0 and n > 0):
        sign = -1
    result = m = abs(m)
    n = abs(n)
    for i in range(n-1):
        result += m
    return sign * result
