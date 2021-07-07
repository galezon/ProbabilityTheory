import math
import numpy.random as random
import numpy as np
import matplotlib.pyplot as plt
import sys
from matplotlib.patches import Ellipse

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])
d = float(sys.argv[4])

def angle(a,b,c,d):
    y = np.array([[a,b],[c,d]])
    h = np.linalg.eig(y)[1]
    return(np.rad2deg(math.atan(h[1][0]/h[1][1])))

def cov(a,b,c,d):
    M = np.array([[a,b],[c,d]])
    Mt = np.transpose(M)
    return( M.dot(Mt))

def normal_vector():
    return (np.array([random.normal(),random.normal()]))


def angle(a,b,c,d):
    y = np.array([[a,b],[c,d]])
    h = np.linalg.eig(y)[1]
    return(np.rad2deg(math.atan(h[1][0]/h[1][1])))


def method1(n,a,b,c,d):
    raw_points = [] #generates 1000 raw points
    while len(raw_points) < n:
        raw_points.append(normal_vector())
    transform = np.array([[a,b],[c,d]])
    result = []
    for i in raw_points:
        result.append(transform.dot(i))
    return result

def method2(n,a,b,c,d,mean=[0,0]):
    result = []
    while len(result) < 1000:
        result.append(random.multivariate_normal(mean,cov(a,b,c,d)))
    return result

def singular(a,b,c,d):
    f = np.linalg.eigvals(cov(a,b,c,d))
    return (f[0]**(0.5),f[1]**(0.5))

def main():
    u = method1(1000,a,b,c,d)
    bx = []
    by = []
    for i in u:
        bx.append(i[0])
        by.append(i[1])
    m2 = method2(1000,a,b,c,d)
    mx = []
    my = []
    for i in m2:
        mx.append(i[0])
        my.append(i[1])
    ax = plt.subplot(111, aspect='equal')
    ell = Ellipse((0,0),6*singular(a,b,c,d)[0],6*singular(a,b,c,d)[1],angle(a,b,c,d),color='red')
    ell.set_facecolor('none')
    ax.add_artist(ell)
    plt.plot(bx, by, 'x')
    plt.axis('equal')
    plt.show()
    ax1 = plt.subplot(211, aspect='equal')
    ell1 = Ellipse((0,0),6*singular(a,b,c,d)[0],6*singular(a,b,c,d)[1],angle(a,b,c,d),color='red')
    ell1.set_facecolor('none')
    ax1.add_artist(ell1)
    plt.plot(mx, my, 'x')
    plt.axis('equal')
    plt.show()
    
    

if __name__ == '__main__':
    main()



