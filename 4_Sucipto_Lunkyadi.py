import matplotlib.pyplot as plt
import random
import sys
import math

def combination(x,y):
    import math
    if y > x:
        raise ValueError
    a = math.factorial(x) / math.factorial(y)
    b = a / math.factorial(x-y)
    return b

n = int(sys.argv[1])
p = float(sys.argv[2])
k = float(sys.argv[3])

def binom_dist(n,p):
    result = []
    k = 0
    while k <= n:
        result.append(combination(n,k)*(p**k)*((1-p)**(n-k)))
        k += 1
    return result

def create_list(k):
    a = [i for i in range(k)]
    b = []
    counter = 0
    for i in a:
        b.append(i-counter)
        counter += 1
    return b


def sim_binom(n,p,k):
    simulate = 0
    counter = 0
    success = 0
    b = create_list(n+1)
    result = []
    while simulate < k:
        while counter < n :
            sim = random.random()
            if sim <= p:
                success += 1
            counter += 1
        b[success] += 1
        counter = 0
        success = 0
        simulate += 1
    for i in b:
        result.append(i/k)
    return result

def poisson_value(i,lam):
    return (lam**i)*(math.exp(- lam))/math.factorial(i)

def poisson_dist(n,p):
    lam = n*p
    res = []
    for i in range(n+1):
        res.append(poisson_value(i,lam))
    return res

def plott(n,p,k):
    x = [i for i in range(n+1)]
    plt.subplot(311)
    plt.bar(x,binom_dist(n,p))
    plt.subplot(312)
    plt.bar(x,sim_binom(n,p,k))
    plt.subplot(313)
    plt.bar(x,poisson_dist(n,p))
    plt.show()

def main():
    plott(n,p,k)


if __name__ == '__main__':
    main()