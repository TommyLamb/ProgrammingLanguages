#Question 5
def evennumbers(n):
    return [list for list in range(2*n) if list % 2 == 0]

#Question 6
def multiples(numberlist):
    return [sublist for sublist in numberlist if sublist % 3 == 0]

#Question 7
def selfzip(listx, listy):
    return [(listx[a],listy[a]) for a in range(max(len(listx),len(listy)))]

#Question 8
def squarepentagonals(length):
    return [x for x in [p*(3*p-1)//2 for p in range(length)] if x in [s*s for s in range(length)]]

squarepentagonals(10)
squarepentagonals(10000)


#Question 9
def nest(n):
    if n == 0:
        return []
    else:
        return [nest(n-1)]
    

def unnest(n):
    try:
        n[0]
        return 1+unnest(n[0])
    except IndexError:
        return 0
    
def nestadd(x,y):
    try:
        x[0]
        return [nestadd(x[0], y)]
    except IndexError:
        return y

def nestmult(x,y):
    z = x
    accum = []
    while True:
        try:
            z[0]
            accum = nestadd(accum,y)
            z = z[0]
        except IndexError:
            return accum


x = nest(5)
y = nest(4)
z = nestadd(x,y)