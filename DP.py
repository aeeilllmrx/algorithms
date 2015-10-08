

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

# knapsack 0/1
def knapsack(items, s, getpath=True):
    '''
    0/1 knapsack problem
    params: 
    items contains triples of the form [name, weight, value]
    s is the maximum weight
    '''
    
    n = len(items)
    # we define a grid with each row representing a number of items
    # and each column representing a different weight sum
    # so (i-1, j-1) := max value obtained by using i items to make maximum j weight

    grid = [[0 for j in range(s+1)] for i in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, s+1):
            
            # by default, pull the value from above
            grid[i][j] = grid[i-1][j]
            
            # if the weight of one of the allowable items is less than
            # the max weight, consider adding it
            if items[i-1][1] <= j:
                
                # in this case we must also consider the residual
                residual_weight = j - items[i-1][1]
                possible_val = items[i-1][2] + grid[i-1][residual_weight]
                grid[i][j] = max(grid[i][j], possible_val)
    
    # save optimal value
    maxval = grid[n][s]
    
    if getpath:
        
        # backtrack through the grid
        path = []
        while s > 0 and n > 0:
            
            # if we didn't inherit from above, we must have taken the item
            if grid[n][s] != grid[n-1][s]:
                path.append(n)
                wt = items[n-1][1]
                n -= 1; s -= wt
            else:
                n -= 1
  
    return maxval, path
            
# word break problem - given a string and a dict of words, 
# can the string be composed of just a subset of those words?
def word_break(s, words):
    
    n = len(s)
    
    # initialize bools
    poss = [False for i in range(n)]
    
    # for each endpoint, see if we can break down prefix string
    # into valid segments
    for i in range(n):
        if s[:i+1] in words:
            poss[i] = True
        for j in range(i):
            if poss[j] and s[j+1:i+1] in words:
                poss[i] = True
                break
    return poss[-1]


def block_stacking():

    pass

def longest_arithmetic_progression():

    pass

