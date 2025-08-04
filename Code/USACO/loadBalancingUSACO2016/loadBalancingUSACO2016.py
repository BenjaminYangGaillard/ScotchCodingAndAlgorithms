import sys

class Fenw:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (self.n + 1)
    
    def update(self, index, delta):
        while index <= self.n:
            self.tree[index] += delta
            index += index & -index

    def find_kth(self, k):
        res = 0
        bit = 1
        while bit < self.n:
            bit <<= 1
        bit //= 2
        
        while bit:
            nxt = res + bit
            if nxt <= self.n and self.tree[nxt] < k:
                k -= self.tree[nxt]
                res = nxt
            bit //= 2
        return res + 1

def main():
    with open('/home/benjamin/SchoolWork/Code/balancing.in') as fin:
        data = fin.read().split()
    if not data:
        return
    
    n = int(data[0])
    cows = []
    max_y = 1000000
    for i in range(n):
        x = int(data[1 + 2*i])
        y = int(data[1 + 2*i + 1])
        cows.append((x, y))
    
    cows.sort(key=lambda p: p[0])
    
    left_tree = Fenw(max_y)
    right_tree = Fenw(max_y)
    
    for (x, y) in cows:
        right_tree.update(y, 1)
    
    ans = n
    
    L = 0
    R = n
    M0 = binary_search_M(L, R, left_tree, right_tree, max_y, n)
    if M0 < ans:
        ans = M0

    for i in range(n):
        x_i, y_i = cows[i]
        right_tree.update(y_i, -1)
        left_tree.update(y_i, 1)
        L = i + 1
        R = n - L
        M0 = binary_search_M(L, R, left_tree, right_tree, max_y, n)
        if M0 < ans:
            ans = M0
            
    with open('balancing.out', 'w') as fout:
        fout.write(str(ans) + '\n')

def binary_search_M(L, R, left_tree, right_tree, max_y, n):
    low_bound = 0
    high_bound = n
    best = n
    while low_bound <= high_bound:
        M = (low_bound + high_bound) // 2
        if check_feasible(M, L, R, left_tree, right_tree, max_y):
            best = M
            high_bound = M - 1
        else:
            low_bound = M + 1
    return best

def check_feasible(M, L, R, left_tree, right_tree, max_y):
    INF = 10**9 + 10
    if L == 0:
        lowL = -INF
        highL = INF
    else:
        if L - M > 0:
            k_val = L - M
            lowL = left_tree.find_kth(k_val)
        else:
            lowL = -INF
            
        if M < L:
            k_val = M + 1
            highL = left_tree.find_kth(k_val)
        else:
            highL = INF
            
    if R == 0:
        lowR = -INF
        highR = INF
    else:
        if R - M > 0:
            k_val = R - M
            lowR = right_tree.find_kth(k_val)
        else:
            lowR = -INF
            
        if M < R:
            k_val = M + 1
            highR = right_tree.find_kth(k_val)
        else:
            highR = INF
            
    low = max(lowL, lowR)
    high = min(highL, highR)
    
    if low >= high:
        return False
        
    candidate_b = low + 1
    if candidate_b % 2 == 1:
        candidate_b += 1
        
    return candidate_b <= high

if __name__ == "__main__":
    main()
