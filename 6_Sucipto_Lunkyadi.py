import math
import numpy as np
import random
import matplotlib.pyplot as plt
import sys

n = int(sys.argv[1])

def method1(n):
    a = [random.random()*2 - 1 for i in range(n)]
    b = [((1-(i**2))**0.5)*2 for i in a]
    b.append(0)
    b.append(2)
    return sorted(b)
    

def method2(n):
    result = []
    for i in range(n):
        angle = random.random()*math.pi*2
        x = math.cos(angle)
        y = math.sin(angle)
        chord = ( (1 - x)**2 + y**2 )**0.5
        result.append(chord)
    result.append(0)
    result.append(2)
    return sorted(result)
    pass
    
    

def gen_points(n):
    result = []
    while len (result) < n:
        x = random.random()*2 - 1
        y = random.random()*2 - 1
        if abs(y) < ( 1 - (x**2) )**0.5:
            result.append((x,y))
    return result

def method3(n):
    chords = []
    points = gen_points(n)
    for i in points:
        a = (i[0]**2 + i[1]**2)**0.5
        length = ( 1 - a**2 )**0.5
        chords.append(length*2)
    chords.append(0)
    chords.append(2)
    return sorted(chords)

def cdf(n):
    x1 = method1(n)
    x2 = method2(n)
    x3 = method3(n)
    y = [i/n for i in range(n)]
    y.insert(0,0)
    y.append(1)
    plt.step(x1,y,'r',x2,y,'g',x3,y,'b')

def main():
    cdf(n)

if __name__ == '__main__':
    main()