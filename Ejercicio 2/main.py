from hash import Hash
import math
import random

if __name__ == "__main__":
    tam = 1000
    Hashing = hash(tam)    
    for i in range(tam-1):
        Hashing.insertar(math.floor(random.randint(1,tam)))
    Hashing.insertar(200)
    print(Hashing.buscar(200))