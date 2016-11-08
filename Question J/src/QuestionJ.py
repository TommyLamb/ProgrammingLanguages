#Question 5
def evennumbers(n):
    return [number for number in range(0,2*n,2)]

evennumbers(10)



#Question 6
def multiples(numberlist):
    return [sublist for sublist in numberlist if sublist % 3 == 0]

multiples(list(range(36)))


#Question 7
def selfzip(listx, listy):
    return [(listx[a],listy[a]) for a in range(max(len(listx),len(listy)))]

selfzip(['a','b','c','d','e','f','g','h','i','j','k','l'],list(range(12)))


#Question 8
def squarepentagonals(length):
    return [x for x in [p*(3*p-1)//2 for p in range(length)] if x in [s*s for s in range(length)]]

squarepentagonals(10)
squarepentagonals(10000)

from math import floor, sqrt
def squarepentagonalgenerator():
    index = 0
    while True:
        x = index*(3*index-1)//2
        if floor(sqrt(x))==sqrt(x):
            yield x
        index += 1

SPNumber = squarepentagonalgenerator()
for i in range(4):
    next(SPNumber)

#Question 9
def nest(n):
    if n == 0:
        return []
    else:
        return [nest(n-1)]

nest(5)


def unnest(n):
    try:
        n[0]
        return 1+unnest(n[0])
    except IndexError:
        return 0

unnest(nest(5))
unnest([[[]]])   


def nestadd(x,y):
    try:
        x[0]
        return [nestadd(x[0], y)]
    except IndexError:
        return y

x = nestadd(nest(5),nest(4))
print(x)
unnest(x)


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


x = nestmult(nest(5), nest(4));
print(x)
unnest(x)
nestmult(nest(0), nest(5));
nestmult(nest(5), nest(0));
nestmult(nest(0), nest(0));
nestmult(nest(2), nest(1));