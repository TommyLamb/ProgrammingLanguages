# Question 1
from math import sqrt, ceil
def isprime(number):
    if (number == 2) or (number == 3):
        return True
    
    if (number % 2 == 0) or (number % 3 == 0):
        return False
    
    for counter in range(5, ceil(sqrt(number)), 6):
        if ((number % counter) == 0) or ((number % (counter + 2)) == 0):
            return False
    return True

def factors(number):
    accumulator = []
    for testcase in range(2, number, 1):
        if (number % testcase == 0) and isprime(testcase):
            accumulator.append(testcase)
    return accumulator

# Question 2
def largest(intlist):
    maxvalue = intlist[0]
    for value in intlist[1:]:
        if maxvalue < value:
            maxvalue = value
    return value

# Question 3
def largest_factor(number):
    return largest(factors(number))

# Question 4
# This program treats the fibonacci sequence as "0,1,1,2...", with "0" as the zeroeth value
def fibonacci(index):
    fiblist = [0, 1]
    if index == 0:  # edge case handling
        return fiblist[0]
    
    while index > (len(fiblist) - 1):
        nextfib = fiblist[-1] + fiblist[-2]
        fiblist.append(nextfib)
    return fiblist[-1]

# Question 5
def firstbigf(number, function):
    count = 1
    while True:
        if len(str(function(count))):
            return count
        count += 1

# Question 7
# The methodology of calculating Pythaogrean triples was taken from Wikipedia: https://en.wikipedia.org/wiki/Formulas_for_generating_Pythagorean_triples#I.
# There are likely more comprehensive/efficient algorithms, but I haven't the mathematical clout to implement them in reasonable time
def triples():
    counter = 2
    previousresult = (4, 3, 5)
    while True:
        yield previousresult
        counter += 1
        nextresulta = previousresult[0] + previousresult[1] + previousresult[2]
        nextresultb = fibonacci((2 * counter) - 1) - previousresult[1]
        nextresultc = fibonacci(2 * counter)
        previousresult = (nextresulta, nextresultb, nextresultc)

