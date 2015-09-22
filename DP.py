

# working through a few dynamic programming exercises

# maximum increasing subsequence
# n^2 solution
def max_inc_sub(lst):

    n = len(lst)
    x = [1] + [0]*(n - 1)
    for i in range(1, n):
        for j in range(i):
            if lst[j] < lst[i] and x[j] + 1 > x[i]:
                x[i] = 1 + x[j]
    return max(x)

# n log n, with patience sorting
def misp(lst):

    n = len(lst)
    piles = [lst[0]]
    pile_len = 1
    for i in range(1, n):
        newp = True
        for j in range(pile_len):
            if lst[i] < piles[j]:
                piles[j] = lst[i]
                newp = False
                break
        if newp:
            piles.append(lst[i])
            pile_len += 1
    return len(piles)

# longest common subsequence
def lcs(a, b):

    m = len(a); n = len(b)

    # initialize grid with zero border
    grid = [[0 for j in range(n+1)] for i in range(m+1)]

    for i in range(m):
        for j in range(n):
            if a[i] == b[j]:
                grid[i+1][j+1] = 1 + grid[i][j]
            else:
                grid[i+1][j+1] = max(grid[i+1][j], grid[i][j+1])

    # for length just get top right value
    num = grid[m][n]

    # for actual sequence you need to backtrack
    path = []

    while m > 0 and n > 0:
        if grid[m][n] == grid[m][n-1]:
            n -= 1
        elif grid[m][n] == grid[m-1][n]:
            m -= 1
        else:
            path.insert(0, a[m-1])
            m -= 1; n -= 1

    return num, path


def bridges(lst):

    pass

def subset_sum():

    pass

def edit_distance():

    pass

def block_stacking():

    pass

def longest_arithmetic_expression():

    pass

def bitonic_tour():

    pass
