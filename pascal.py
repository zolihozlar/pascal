import math

# pascals_tri_formula = [] # don't collect in a global variable.

def combination(n, r): # correct calculation of combinations, n choose k
    return int((math.factorial(n)) / ((math.factorial(r)) * math.factorial(n - r)))

def for_test(x, y): # don't see where this is being used...
    for y in range(x):
        return combination(x, y)

# def digitalSum(n):
#     if n < 10 :
#         return n
#     return n % 10 + digitalSum( n // 10 )

# def digitalSum(n):
#   def process(n, sum):
#     if n < 10:
#       return sum + n
#     return process(n / 10, sum + n % 10)
#   return process(n, 0)

def digitalSum (n):
    n = abs(int(n))
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

def pascals_triangle(rows):
    result = [] # need something to collect our results in
    # count = 0 # avoidable! better to use a for loop, 
    # while count <= rows: # can avoid initializing and incrementing 
    for count in range(rows): # start at 0, up to but not including rows number.
        # this is really where you went wrong:
        row = [] # need a row element to collect the row in
        for element in range(count + 1): 
            # putting this in a list doesn't do anything.
            # [pascals_tri_formula.append(combination(count, element))]
            row.append(digitalSum(combination(count, element)))
        result.append(row)
        # count += 1 # avoidable
    return result

# now we can print a result:
for row in pascals_triangle(16384):
    # print(row)
    print('|'.join(str(v) for v in row))
