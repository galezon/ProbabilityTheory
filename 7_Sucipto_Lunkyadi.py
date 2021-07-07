import math
import random
import scipy.integrate as integrate

def generate(n):
    a = []
    while len(a) < n:
        a.append( random.random())
    a.sort()
    return (a)

def sim(a):
    b = []
    for i in a:
        if i <= 0.25:
            b.append(i**0.5)
        if 0.25 < i <= 0.5:
            b.append(0.5)
        if i > 0.5:
            b.append( (3*i) - 1)
    return ( b )

def calc(a):
    count = 0
    for i in a:
        if i == 0.5:
            count += 1
    return count

def avg(b):
    sum = 0
    for i in b:
        sum += i
    return sum/len(b)

def ex_v():
    return integrate.quad(lambda x : 1 - x**2,0,0.5)[0] + integrate.quad(lambda x : 1 - ((x+1)/3),0.5,2 )[0]

def main():
    a = generate(1000)
    b = sim(a)
    c = avg(b)
    d = calc(b)
    e = ex_v()
    f = 0.25
    print("{:.5f}{:5}{:.5f}".format(c,'    ',d))
    print("{:.5f}{:5}{:.5f}".format(e,'    ',f))

if __name__ == "__main__":
    main()