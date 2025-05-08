from functools import lru_cache

def Fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

for i in range(1, 500):
    print(i, ":", Fibonacci(i))

cache = {}

def fib2(n):
    if n in cache:
        return cache[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib2(n - 1) + fib2(n - 2)
    cache[n] = result
    return result

for i in range(1, 1000):
    print(f"{i} Term: {fib2(i)}")

@lru_cache(maxsize=1000)
def fib3(n):
    if n == 1 or n == 2:
        return 1
    return fib3(n - 1) + fib3(n - 2)

for i in range(1, 1000):
    print(i, ":", fib3(i))

def TowerofHanoi(n, source, destination_rod, auxiliary_rod):
    if n == 1:
        print(f"Move disk 1 from source {source} to destination {destination_rod}")
        return
    TowerofHanoi(n - 1, source, auxiliary_rod, destination_rod)
    print(f"Move disk {n} from source {source} to destination {destination_rod}")
    TowerofHanoi(n - 1, auxiliary_rod, destination_rod, source)

n = 3
TowerofHanoi(n, 'A', 'B', 'C')



