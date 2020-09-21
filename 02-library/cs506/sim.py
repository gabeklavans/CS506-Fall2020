import math

def euclidean_dist(x, y):
    if len(x) != len(y):
        return "Can't take similarity of vectors in different dimensions"

    total = 0
    for i in range(len(x)):
        total += (x[i]-y[i])**2

    return math.sqrt(total)

def manhattan_dist(x, y):
    if len(x) != len(y):
        return "Can't take similarity of vectors in different dimensions"

    ret = 0
    for i in range(len(x)):
        ret += abs(x[i] - y[i])

    return ret

# Simlarity algo lifted from https://stackoverflow.com/a/52059258
def jaccard_dist(x, y):
    if (x == y):
        return 0

    s1 = set(x)
    s2 = set(y)
    return 1 - len(s1.intersection(s2)) / len(s1.union(s2))

def cosine_sim(x, y):
    if len(x) != len(y):
        return "Can't take similarity of vectors in different dimensions"

    dotProd = 0
    xSum = 0
    ySum = 0
    for i in range(len(x)):
        dotProd += x[i] * y[i]
        xSum += x[i]
        ySum += y[i]

    xMag = math.sqrt(xSum)
    yMag = math.sqrt(ySum)

    if xMag == 0 or yMag == 0:
        return math.inf

    return dotProd / (xMag * yMag)

# Feel free to add more
