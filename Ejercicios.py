import queue

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primos_hasta_n(n):
    q = queue.Queue()

    for i in range(2, n + 1):
        if es_primo(i):
            q.put(i)

    while not q.empty():
        print(q.get())

# Imprimir números primos entre 1 y 1000
primos_hasta_n(1000)