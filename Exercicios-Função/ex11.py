def encontrar_divisor(n):
    return [i for i in range(1, n + 1) if n % i == 0]

print(encontrar_divisor(35))
