def fibonacci(n):
    fib_series = [0, 1]
    for i in range(2, n):
        next_term = fib_series[-1] + fib_series[-2]
        fib_series.append(next_term)
    return fib_series

n = int(input("Ingrese un número para la serie Fibonacci: "))
print(fibonacci(n))
