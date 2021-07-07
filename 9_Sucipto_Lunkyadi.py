import math
import random
import sys

n = int(sys.argv[1])
L = int(sys.argv[2])

def simulate(n,L):
    result = []
    while len(result) < n :
        theta = random.random()*( math.pi/2) #angle, always positive on 1st quadrant
        d = random.random()/2 #distance of center from the closest parallel line
        l = (L/2) * math.cos(theta) #length of the horizontal part of the needle (along x-axis)
        lines_close = ( (l - d)//1 ) + 1 #side closer to center, +1 because after we subtract (l-d), it already crosses the first line
        lines_far = ( (l - (1-d))//1 ) + 1 #side further from the center, distance of center to the other parallel line is 1-d
        result.append(lines_close + lines_far) #total number of lines we cross on either side
    return result

def create(L):
    result = [i for i in range(int((L//1)+2))]
    i = 0
    while i <= result[-1]:
        result[i] -= i
        i += 1                      
    return result

def calculate(res,L):
    result = create(L) #creates a list with zero as values
    for i in res:
        result[int(i)] += 1
    return result

def main():
    x = simulate(n,L)
    y = calculate(x,L)
    i = 0
    print( ('x','P(X=x)'))
    while i < len(y):
        print( (i,y[i]/n) )
        i += 1
    print( (2*L)/(y[1]/n) )

if __name__ == "__main__":
    main()

