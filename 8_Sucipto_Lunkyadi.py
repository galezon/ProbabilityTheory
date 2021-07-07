import math
import random
import numpy as np
import matplotlib.pyplot as plt
step = 1/50
t = np.arange(0, 1 + step, step)

def simulate_RV(n):
    result = []
    while len(result) < n:
        a = [random.random() for i in range(10)]
        a.sort()
        result.append(a[7])
    return sorted(result)

def func_a(x):
    a = math.factorial(10)
    b = math.factorial(7)
    c = math.factorial(2)
    return( a * (x**7) * (1-x)**2 / (b*c))

def func_b(x):
    a = math.factorial(10)
    b = math.factorial(6)
    c = math.factorial(3)
    return ( a * (x**6) * (1-x)**3 / (b*c) )

def hist():
    step = 1/50
    t = np.arange(0, 1 + step, step)
    plt.hist(simulate_RV(5000), bins=50, density=1)

def main():
    a1 = np.linspace(0,1,10000)
    b1 = [func_a(i) for i in a1]
    c1 = [func_b(i) for i in a1]
    plt.plot(a1,b1)
    plt.plot(a1,c1)
    hist()
    plt.show()
    a = simulate_RV(5000)
    fa = [func_a(i)*random.random() for i in a]
    fb = [func_b(i)*random.random() for i in a]
    la = [func_a(i) for i in a]
    lb = [func_b(i) for i in a]
    plt.subplot(121)
    plt.plot(a,fa,'r.')
    plt.plot(a,la)
    plt.subplot(122)
    plt.plot(a,fb,'r.')
    plt.plot(a,lb)
    plt.show()
    print('I think function a is the proper density function. We multiplied each value of f(x) with random.random(), this would result in if a column has a lot of points (the density is high), it will be evenly spread out across the column. This should yield us a relatively evenly spread out graph. However, for function b, if we compare the left and the right side, points that should have equal density have different number of points plotted. The cloud of points is not evenly spread out. Thus, b is not the proper density function.')

if __name__ == "__main__":
    main()
