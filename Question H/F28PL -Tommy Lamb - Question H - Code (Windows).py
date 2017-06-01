# Question 1
def mult1(numberlist):
    accumulator = 1
    for x in numberlist:
        accumulator *= x
    return accumulator

mult1([])
mult1([1,2,3,4,5])
mult1([4,3,2])
mult1([0])


# Question 2
def mult2(numberlist):
    if len(numberlist) == 0:
        return 1
    else:
        return numberlist.pop() * (mult2(numberlist))

mult2([])
mult2([1,2,3,4,5])
mult2([4,3,2])
mult2([0])


# Question 3
mult2(list(range(10 ** 100))) #Range greater than list structure size limit

mult2(list(range(1001))) #Recursion limit error


# Question 4
from functools import reduce
def mult3(numberlist):
    return reduce(lambda x, y: x * y, numberlist, 1)

mult3([])
mult3([1,2,3,4,5])
mult3([4,3,2])
mult3([0])


# Question 5
mult1([1.0, 2, 3.0, 10])
mult2([1.0, 2, 3.0, 10])
mult3([1.0, 2, 3.0, 10])
# All return 60.0


# Question 7
def multpoly(polylist):
    accumulator = polylist[0]
    for entry in polylist[1:]:
        if type(entry) is int:
            accumulator *= entry
        else:
            accumulator += entry
    return accumulator

multpoly([]) # "We do not care what multpoly calculates on the empty list."
multpoly([0])
multpoly([1,2,3,4,5])
multpoly(['a','b','c','d','e','f','g'])
multpoly(['a',3,'b','c',100]) # due to implementation, some funky effects can be achieved
multpoly(['a',3,multpoly(['b',7]),10,multpoly(['Y',15, multpoly(["Alpha", 3, "Beta", 2]), 3]), 20])
multpoly([1,2,'a']) #However, types can only be mixed if the first element is a string or list


# Question 8
# This method was derived from http://stackoverflow.com/a/2158522
def flatten(nestedlist):
    if type(nestedlist) is list:
        return [elements for lists in nestedlist for elements in flatten(lists)]
    else:
        return [nestedlist]  # nestedlist isn't actually a list in this case.

flatten([])
flatten(['Hi', 5])
flatten([['The'],'quick', [['brown'], 'fox'], [[['jumped', 'over'], 'the', ['lazy',[[['Data', ]]]]]], 'structure'])