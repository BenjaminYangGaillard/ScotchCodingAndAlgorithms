import itertools
import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def permutation_order(p):
    n = len(p)
    visited = [False] * n
    order = 1
    for i in range(n):
        if not visited[i]:
            length = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = p[j]
                length += 1
            order = lcm(order, length)
    return order

def main():
    
    with open("exercise.in", "r") as f:
        N, M = map(int, f.readline().split())
    
    perms = itertools.permutations(range(N))
    from collections import Counter
    count_by_order = Counter()

    for perm in perms:
        order = permutation_order(perm)
        count_by_order[order] += 1

    result = 1
    for order, count in count_by_order.items():
        result = (result * pow(order, count, M)) % M

    with open("exercise.out", "w") as f:
        f.write(str(result) + "\n")

if __name__ == "__main__":
    main()

